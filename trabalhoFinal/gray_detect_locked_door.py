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


def is_door_locked(test_image_path, base_image_path, tolerance):
    test_image = cv2.imread(test_image_path)
    base_image = cv2.imread(base_image_path)
    lower_color_rgb = (60, 60, 60)
    upper_color_rgb = (100, 100, 100)

    test_image_pixels = count_filtered_pixels(
        test_image, lower_color_rgb, upper_color_rgb
    )
    base_image_pixels = count_filtered_pixels(
        base_image, lower_color_rgb, upper_color_rgb
    )

    if test_image_pixels > base_image_pixels + tolerance:
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


tolerance = int(input("Digite a margem de erro de cinza: "))
for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    if i < 4:
        image1 = test_images[i]
        image2 = unlocked_images[0]
    else:
        image1 = test_images[i]
        image2 = locked_images[0]

    plt.title(
        "Trancado" if is_door_locked(image1, image2, tolerance) else "Destrancado"
    )
    image = Image.open(image1)
    compressed_image = image.resize((500, 500))
    plt.imshow(ndimage.rotate(compressed_image, -90))
    plt.axis("off")
    i += 1

plt.show()
