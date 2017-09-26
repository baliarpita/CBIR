# import the necessary packages
# test.py displays the masks and the RGB masked image
# 5 Masks are created.
# test.py demonstrates the concept of including pixels in the histogram with a
# corresponding mask value of white
# test.py is a demo class implementation of ColorDescriptor.py

import numpy as np
import cv2

class ColorDescriptor:

	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins

	def describe(self, image):
		# convert the image to the HSV color space and initialize
		i=image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]

		# construct an elliptical mask representing the center of the image
		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# loop over the segments
		for (startX, endX, startY, endY) in segments:

			# construct a mask for each corner of the image, subtracting
			# the elliptical center from it
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)

			# display corner masks for the HSV image
			cv2.imshow("Corner Mask",cornerMask)
			key=cv2.waitKey(0)

			# extract masked image using HSV image and corner masks
			masked=cv2.bitwise_and(i,i,mask=cornerMask)

			# display the corner masked images
			cv2.imshow("Masked Corner Image",masked)
			key=cv2.waitKey(0)

			# extract masked image using HSV mage and elliptical masks
			cv2.imshow("Ellipse Mask",ellipMask)
			key=cv2.waitKey(0)

		# display the ellipse masked image
		masked=cv2.bitwise_and(i,i,mask=ellipMask)
		cv2.imshow("Masked Elliptical Image",masked)
		key=cv2.waitKey(0)

# using ColorDescriptor class, describe the image descriptor (3D HSV Color Model)
# and read an image to mask and plot
image=cv2.imread("101401.png")
ColorDescriptor((8,12,3)).describe(image)