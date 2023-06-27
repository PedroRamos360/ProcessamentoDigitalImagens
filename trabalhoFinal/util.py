import cv2
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def cshow(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, WINDOW_WIDTH, WINDOW_HEIGHT)
    cv2.imshow(window_name, image)


def load_image(window_name, image):
    cshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def count_filtered_pixels(image, lower_color, upper_color):
    mask = cv2.inRange(image, lower_color, upper_color)
    num_filtered_pixels = np.count_nonzero(mask)

    return num_filtered_pixels


def filter_color(image, lower_color, upper_color):
    mask = cv2.inRange(image, lower_color, upper_color)
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image


# def difference_between_locked_and_unlocked():
#     locked_image = cv2.imread(IMAGE_LOCKED)
#     unlocked_image = cv2.imread(IMAGE_UNLOCKED)
#     lower_color_rgb = (60, 60, 60)
#     upper_color_rgb = (100, 100, 100)

#     locked_image_pixels = count_filtered_pixels(
#         locked_image, lower_color_rgb, upper_color_rgb
#     )
#     unlocked_image_pixels = count_filtered_pixels(
#         unlocked_image, lower_color_rgb, upper_color_rgb
#     )

#     return locked_image_pixels - unlocked_image_pixels


def is_door_locked(test_image_path, unlocked_image_path, tolerance):
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

    if test_image_pixels > unlocked_image_pixels + tolerance:
        return True
    else:
        return False


# def load_images():
#     for image_path in [IMAGE_LOCKED, IMAGE_UNLOCKED]:
#         image = cv2.imread(image_path)

#         lower_color_rgb = (60, 60, 60)  # example lower green value in BGR
#         upper_color_rgb = (100, 100, 100)  # example upper green value in BGR

#         filtered_image = filter_color(image, lower_color_rgb, upper_color_rgb)
#         cshow("Filtered Image", filtered_image)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
