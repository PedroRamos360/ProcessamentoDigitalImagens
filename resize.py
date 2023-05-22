import cv2

# Load the image
image = cv2.imread('images/tree.jpg')

# Define the desired width and height for the resized image
desired_width = int(input("Type desired width: "))
desired_height = int(input("Type desired height: "))

# Resize the image
resized_image = cv2.resize(image, (desired_width, desired_height))

cv2.imwrite("images/resized_image.jpg", resized_image)
