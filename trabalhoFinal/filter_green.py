from custom_imshow import *
from images import *

import cv2
import numpy as np


def filter_green(image):
    # Convert image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for green color in HSV
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # Create a mask for green color
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Bitwise AND operation to extract green color
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image


# Load the image
image_path = IMAGE_TEST
image = cv2.imread(image_path)

# Apply green color filtering
filtered_image = filter_green(image)

# Display the original and filtered images
cshow("Original Image", image)
cshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
target_color = (255, 0, 0)  # For example, blue color
