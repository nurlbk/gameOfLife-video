import random
import time

import gameOfLife
from PIL import Image
import numpy as np
import cv2
WIDTH = 320
HEIGHT = 180
NUM_OF_ITERATIONS = 360
POINTS_RATE = 20
frameSize = (WIDTH * 4, HEIGHT * 4)
FPS = 24


def to_video():
    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), FPS, frameSize)

    for i in range(NUM_OF_ITERATIONS):
        img = cv2.imread(f'photos/pic{i + 1}.png')
        out.write(img)

    out.release()


def to_png(data, i):
    img = img_grey(np.array(data))
    img_resized = img.resize((WIDTH * 4, HEIGHT * 4))
    img_resized.save(f'photos/pic{i + 1}.png', format='png')


def img_grey(data):
    return Image.fromarray(data).convert('1')


def main():
    lf = gameOfLife.Life(HEIGHT, WIDTH)
    lf.random_select(POINTS_RATE)

    for i in range(NUM_OF_ITERATIONS):
        to_png(lf.state, i)
        lf.nextstate()
        time.sleep(0.25)

    to_video()


if __name__ == '__main__':
    main()
