"""Script to create data files."""

import cv2
import os

img_path = 'data_img.jpg'

img = cv2.imread(img_path, 0)

for x in range(img.shape[1]):
    os.mkdir('data/{}'.format(x))
    for y in range(img.shape[0]):
        roi = img[y:y + 60, x:x + 60]
        cv2.imwrite('data/{}/{}_{}.png'.format(x, x, y), roi)
    print('[INFO]Completed {} - {} more to go'.format(x, img.shape[1] - x))

"""
The above draws a window of size 60 X 60, then crops it and saves it.

Through manual inspection,
first step is to categorize into text, no text

Second step would be categorize the valid ones to respective class folders

"""

for i in range(10, 511):
    