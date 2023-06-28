import os
import cv2


def filter_color(image, lower_color, upper_color):
    mask = cv2.inRange(image, lower_color, upper_color)
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image


def cshow(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    cv2.imshow(window_name, image)


locked_images_path = "doors/locked"
unlocked_images_path = "doors/unlocked"

locked_images = []
unlocked_images = []

for file_name in os.listdir(locked_images_path):
    locked_images.append(os.path.join(locked_images_path, file_name))

for file_name in os.listdir(unlocked_images_path):
    unlocked_images.append(os.path.join(unlocked_images_path, file_name))

lower_color_rgb = (60, 60, 60)
upper_color_rgb = (100, 100, 100)

cshow(
    "Porta trancada",
    filter_color(cv2.imread(locked_images[0]), lower_color_rgb, upper_color_rgb),
)

cshow(
    "Porta destrancada",
    filter_color(cv2.imread(unlocked_images[0]), lower_color_rgb, upper_color_rgb),
)
cv2.waitKey(0)
