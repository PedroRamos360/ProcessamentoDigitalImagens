import cv2

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def cshow(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, WINDOW_WIDTH, WINDOW_HEIGHT)
    cv2.imshow(window_name, image)
