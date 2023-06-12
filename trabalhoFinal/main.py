from images import *
from custom_imshow import *

import cv2
import numpy as np


def count_filtered_pixels(image, lower_color, upper_color):
    # Create a mask for the specified color range
    mask = cv2.inRange(image, lower_color, upper_color)

    # Count the number of non-zero pixels in the mask
    num_filtered_pixels = np.count_nonzero(mask)

    return num_filtered_pixels


def filter_color(image, lower_color, upper_color):
    # Create a mask for green color
    mask = cv2.inRange(image, lower_color, upper_color)

    # Bitwise AND operation to extract green color
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image


def is_door_locked(test_image_path, unlocked_image_path):
    test_image = cv2.imread(test_image_path)
    unlocked_image = cv2.imread(unlocked_image_path)
    lower_color_rgb = (60, 60, 60)
    upper_color_rgb = (100, 100, 100)

    test_image_pixels = count_filtered_pixels(
        test_image, lower_color_rgb, upper_color_rgb
    )
    unlocked_image_pixels = count_filtered_pixels(
        unlocked_image, lower_color_rgb, upper_color_rgb
    )

    if test_image_pixels > unlocked_image_pixels:
        cshow("Door is locked", test_image)
    else:
        cshow("Door is unlocked", test_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def load_images():
    for image_path in [IMAGE_LOCKED, IMAGE_UNLOCKED]:
        image = cv2.imread(image_path)

        lower_color_rgb = (60, 60, 60)  # example lower green value in BGR
        upper_color_rgb = (100, 100, 100)  # example upper green value in BGR

        filtered_image = filter_color(image, lower_color_rgb, upper_color_rgb)
        cshow("Filtered Image", filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


print(is_door_locked(IMAGE_LOCKED, IMAGE_UNLOCKED))
