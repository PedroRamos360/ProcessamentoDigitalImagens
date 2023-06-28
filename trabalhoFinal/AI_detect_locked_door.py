import matplotlib.pyplot as plt
import tensorflow as tf
import scipy.ndimage as ndimage
import os

num_skipped = 0
for folder_name in ("locked", "unlocked"):
    folder_path = os.path.join("doors", folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            with open(fpath, "rb") as fobj:
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        except:
            is_jfif = False

        if not is_jfif:
            num_skipped += 1
            os.remove(fpath)

print("Deleted %d images" % num_skipped)

image_size = (500, 500)
batch_size = 128
label_names = ["Trancado", "Destrancado"]

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "doors",
    validation_split=0.2,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.axis("off")
        plt.imshow(ndimage.rotate(images[i].numpy().astype("uint8"), -90))
        plt.title(label_names[int(labels[i])])

plt.show()
