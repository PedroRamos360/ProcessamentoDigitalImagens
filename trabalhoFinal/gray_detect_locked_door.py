import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
import scipy.ndimage as ndimage
from PIL import Image


def count_filtered_pixels(image, lower_color, upper_color):
    mask = cv2.inRange(image, lower_color, upper_color)
    num_filtered_pixels = np.count_nonzero(mask)

    return num_filtered_pixels


def is_door_locked(test_image_path, base_image_locked_path, base_image_unlocked_path):
    test_image = cv2.imread(test_image_path)
    base_image_locked = cv2.imread(base_image_locked_path)
    base_image_unlocked = cv2.imread(base_image_unlocked_path)
    lower_color_rgb = (60, 60, 60)
    upper_color_rgb = (100, 100, 100)

    test_image_pixels = count_filtered_pixels(
        test_image, lower_color_rgb, upper_color_rgb
    )
    base_image_locked_pixels = count_filtered_pixels(
        base_image_locked, lower_color_rgb, upper_color_rgb
    )

    base_image_unlocked_pixels = count_filtered_pixels(
        base_image_unlocked, lower_color_rgb, upper_color_rgb
    )

    test_diff_locked = abs(test_image_pixels - base_image_locked_pixels)
    test_diff_unlocked = abs(test_image_pixels - base_image_unlocked_pixels)

    if test_diff_unlocked > test_diff_locked:
        return True
    else:
        return False


locked_images_path = "doors/locked"
unlocked_images_path = "doors/unlocked"

locked_images = []
unlocked_images = []

for file_name in os.listdir(locked_images_path):
    locked_images.append(os.path.join(locked_images_path, file_name))

for file_name in os.listdir(unlocked_images_path):
    unlocked_images.append(os.path.join(unlocked_images_path, file_name))

test_images = []
for i in range(4):
    test_images.append(locked_images[i])

for i in range(5):
    test_images.append(unlocked_images[i])


for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    test_image = test_images[i]

    plt.title(
        "Trancado"
        if is_door_locked(test_images[i], locked_images[0], unlocked_images[0])
        else "Destrancado"
    )
    image = Image.open(test_image)
    compressed_image = image.resize((500, 500))
    plt.imshow(ndimage.rotate(compressed_image, -90))
    plt.axis("off")
    i += 1

plt.show()
