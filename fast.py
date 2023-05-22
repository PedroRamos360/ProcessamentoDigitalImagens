import cv2
import numpy as np
cmg = cv2.imread('images/resized_image.jpg')
gray = cv2.cvtColor(cmg,cv2.COLOR_BGR2GRAY)
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(cmg,None)
img2 = cv2.drawKeypoints(cmg, kp,outImage = None, color=(255,0,0))
# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(cmg, None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv2.drawKeypoints(cmg, kp, None, color=(255,0,0))

cv2.imshow('fast_true',img3)
cv2.waitKey(0)