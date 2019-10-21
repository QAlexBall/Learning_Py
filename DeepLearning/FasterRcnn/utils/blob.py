import numpy as np
import cv2


def im_list_to_blob(images):
    """ Convert a list of images to a network input"""
    max_shape = np.array([image.shape for image in images]).max(axis=0)
    num_images = len(images)