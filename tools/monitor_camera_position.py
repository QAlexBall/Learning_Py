import os
import cv2
import sys
import json
import time
import boto3
import argparse
import datetime
import numpy as np
import urllib.request
from threading import Timer
from bs4 import BeautifulSoup
from collections.abc import Iterable
sys.path.append('..')
from slack_utils import send_slack_alert

MONTH_TO_STRING = {6: 'Jun', 7: 'Jul', 8: 'Aug'}
def send_to_slack(message, up=False):
    payload = {"text": " %s" % (message)}
    send_slack_alert(payload)

def download_current_hour_folder(bucket_name, stream):
    utc_time = datetime.datetime.utcnow()
    print(utc_time)
    stream_path = str(bucket_name) + '/' + str(stream)
    cmd = 'rm -rf ./{}/current && mkdir ./{}/current/ && aws s3 sync s3://{}/{}/{}/{}/{}/annotated ./{}/current/'.format(
        stream_path,
        stream_path,
        bucket_name,
        stream,
        MONTH_TO_STRING[utc_time.month],
        utc_time.day,
        utc_time.hour,
        stream_path
    )
    try: 
        if not os.path.exists('./{}'.format(bucket_name)):
            os.system('mkdir ./{}'.format(bucket_name))
        else:
            if not os.path.exists('./{}'.format(stream_path)):
                os.system('mkdir ./{}'.format(stream_path))
        os.system(cmd)
        return True
    except Exception:
        print('can not download this folder')

def find_feature(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kpts, descs = sift.detectAndCompute(gray, None)
    return image, kpts, descs

def match_image(img1, kpts1, descs1, img2, kpts2, descs2):
    matcher = cv2.FlannBasedMatcher(dict(algorithm = 1, trees = 5), {})
    matches = matcher.knnMatch(descs1, descs2, 2)
    matches = sorted(matches, key = lambda x:x[0].distance)
    good = [m1 for (m1, m2) in matches if m1.distance < 0.75 * m2.distance]
    canvas = img2.copy()
    dst = None
    if len(good) > 1:
        src_pts = np.float32([ kpts1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kpts2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        if (isinstance(M, Iterable)):
            h,w = img1.shape[:2]
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)
            cv2.polylines(canvas,[np.int32(dst)],True,(0,255,0),3, cv2.LINE_AA)
            matched = cv2.drawMatches(img1, kpts1, canvas, kpts2, good, None)#,**draw_params)
            perspectiveM = cv2.getPerspectiveTransform(np.float32(dst),pts)
            found = cv2.warpPerspective(img2,perspectiveM,(w,h))
            cv2.imshow('matched', matched);
            cv2.imshow('found', found);
            cv2.waitKey(1000);
            cv2.destroyAllWindows()
    else:
        print("can't find enough feature point")
    return dst

def find_offset_with_current_folder(bucket_name, stream, img1, kpts1, descs1, x1, x2, y1, y2):
    camera_state = "notmove"
    path = './{}/{}/current/'.format(bucket_name, stream)
    images = os.listdir(path)
    camera_state = 'notmove'
    may_moved_count = 0
    for im in images:
        if im != 'annotated':
            print(path + im)
            image = cv2.imread(path + im)
            img2, kpts2, descs2 = find_feature(image)
            dst = match_image(img1,kpts1, descs1, img2, kpts2, descs2)
            if dst is not None:
                print('x: ' + str(y1 - dst[0][0][1]) + ':' + str(y2 - dst[2][0][1]))
                print('y: ' + str(x1 - dst[0][0][0]) + ':' + str(x2 - dst[2][0][0]))
                if abs(x1 - dst[0][0][0]) > 5 or abs(y1 - dst[0][0][1]) > 5 or abs(x2 - dst[2][0][0]) > 5 or abs(y2 - dst[2][0][1]) > 5:
                    print('==> * moved * <==')
                    may_moved_count += 1
                else:
                    may_moved_count = 0
                    print('==> * not move * <==')
            print("===> may_moved_count ", may_moved_count)
            print('\n')
    # may_moved_count 
    if may_moved_count >= 5:
        camera_state = 'moved'
    return camera_state


def get_first_image_feature(bucket_name, stream):
    first_image = './{}/{}/current_image.jpg'.format(bucket_name, stream)
    for image in os.listdir('./{}/{}/current'.format(bucket_name, stream)):
        os.system('cp ./{}/{}/current/{} {}'.format(bucket_name, stream, image, first_image))
        break
    os.system('labelImg {}'.format(first_image))
    os.system('mv ./current_image.xml ./{}/{}/'.format(bucket_name, stream))

    first_image_xml = './{}/{}/current_image.xml'.format(bucket_name, stream)
    soup = BeautifulSoup(open(first_image_xml), 'xml')
    x1, x2 = int(soup.xmin.string), int(soup.xmax.string)
    y1, y2 = int(soup.ymin.string), int(soup.ymax.string)
    first_im = cv2.imread(first_image)
    crop_img = first_im[y1:y2, x1:x2]
    img, kpts, descs = find_feature(crop_img)
    cv2.imwrite('./{}/{}/first_croped_image.jpg'.format(bucket_name, stream), crop_img)
    return img, kpts, descs, x1, x2, y1, y2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Monitor camera moved!")
    parser.add_argument('-b', '--bucket_name', required=True)
    parser.add_argument('-s', '--stream', required=True)
    parser.add_argument('-hour', '--hour', help='wait time')
    args = parser.parse_args()

    bucket_name = args.bucket_name
    stream = args.stream
    sleep_time = 1800
    if args.hour:
        sleep_time = int(float(args.hour) * 60 * 60)

    download_current_hour_folder(bucket_name, stream)
    print("download_current_hour_folder done!")
    img1, kpts1, descs1, x1, x2, y1, y2 = get_first_image_feature(bucket_name, stream)
    while True:
        success = download_current_hour_folder(bucket_name, stream)
        if success:
            camera_state = find_offset_with_current_folder(bucket_name, stream, img1, kpts1, descs1, x1, x2, y1, y2)
            if camera_state == 'moved':
                send_to_slack(stream + 'camera moved')
        print('wait {} hour...'.format(sleep_time / 60 / 60))
        time.sleep(sleep_time)

'''
def find_offset_with_current_image(bucket_name, stream, img1, kpts1, descs1, x1, x2, y1, y2):
    camera_state = "notmove"
    image = cv2.imread('./{}/{}/current_image.jpg'.format(bucket_name, stream))
    img2, kpts2, descs2 = find_feature(image)
    dst = match_image(img1,kpts1, descs1, img2, kpts2, descs2)
    if dst is not None:
        print('x: ' + str(y1 - dst[0][0][1]) + ':' + str(y2 - dst[2][0][1]))
        print('y: ' + str(x1 - dst[0][0][0]) + ':' + str(x2 - dst[2][0][0]))
        may_moved_count = 0
        if abs(x1 - dst[0][0][0]) > 10 or abs(y1 - dst[0][0][1]) > 10 or abs(x2 - dst[2][0][0]) > 10 or abs(y2 - dst[2][0][1]) > 10:
            print('==> * moved * <==')
            may_moved_count += 1
            # if may moved count > a number, defined camera_state moved
            if may_moved_count >= 1:
                camera_state = 'moved'
        else:
            may_moved_count = 0
            print('==> * not move * <==')
        print('\n')
    return camera_state
'''