import cv2

# Load the image
image = cv2.imread('images/tree.jpg')

# Define the JPEG compression quality (0-100, higher means better quality but larger file size)

compression_quality = int(input("Type compress quality: "))

# Compress and save the image as a JPEG
cv2.imwrite('images/compressed_image.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, compression_quality])
