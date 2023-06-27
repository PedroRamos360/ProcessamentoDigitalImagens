from util import *
import os
import matplotlib.pyplot as plt

folder_path = "doors/locked"

image_files = []

for file_name in os.listdir(folder_path):
    image_files.append(os.path.join(folder_path, file_name))

for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    image = plt.imread(image_files[i])
    plt.imshow(image)
    plt.axis("off")
    i += 1

plt.show()


# tolerance = int(input("Digite a margem de erro de cinza: "))
# locked = is_door_locked(IMAGE_LOCKED, IMAGE_UNLOCKED, tolerance)
