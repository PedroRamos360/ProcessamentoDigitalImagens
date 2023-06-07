import cv2
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGE_LOCKED = "images/locked.jpg"
IMAGE_UNLOCKED = "images/unlocked.jpg"
IMAGE_TEST = "images/test.jpg"


def custom_imshow(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, WINDOW_WIDTH, WINDOW_HEIGHT)
    cv2.imshow(window_name, image)


# def filter_gray_tones(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     median_value = np.median(gray)
#     threshold = 25
#     mask = cv2.inRange(gray, median_value - threshold, median_value + threshold)
#     filtered_image = cv2.bitwise_and(image, image, mask=mask)

#     return filtered_image

# for image_path in [IMAGE_LOCKED, IMAGE_UNLOCKED]:
#     image = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

#     edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
#     # custom_imshow(image_path, img_blur)
#     custom_imshow(image_path, filter_gray_tones(image_path))

# cv2.waitKey(0)

### colors in BGR
low = np.uint8([[[0, 0, 0]]])
high = np.uint8([[[0, 255, 0]]])
print(
    cv2.cvtColor(low, cv2.COLOR_BGR2HSV),
    cv2.cvtColor(high, cv2.COLOR_BGR2HSV),
)


for image_path in [IMAGE_TEST]:
    img = cv2.imread(image_path)

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create the Mask
    mask = cv2.inRange(
        imgHSV,
        cv2.cvtColor(low, cv2.COLOR_BGR2HSV),
        cv2.cvtColor(high, cv2.COLOR_BGR2HSV),
    )
    # inverse mask
    mask = 255 - mask
    res = cv2.bitwise_and(img, img, mask=mask)

    custom_imshow(image_path, res)
    custom_imshow("original", img)
cv2.waitKey(0)
