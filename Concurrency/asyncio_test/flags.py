import os
import time
import sys

import requests
import pdb
POP20_CC = ('IN US ID PK NG RU JP '
            'MX PH VN ET EG DE IR TR FR').split()

BASE_URL = 'https://www.baidu.com'
DEST_DIR = 'downloads/'

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    print("@save_flags", path)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.git'.format(BASE_URL, cc=cc.lower())
    print(url)
    #  pdb.set_trace()
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, str(cc) + '.txt')

    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)


