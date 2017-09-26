# import the necessary packages
# mask.py displays the masks and the masked HSV image
# 5 Masks are created
# mask.py is a demo class implementation of ColorDescriptor.py

import numpy as np
import cv2

class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		self.bins = bins

	def describe(self, image):
		# convert the image to the HSV color space
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]

		# construct an elliptical mask representing the center of the
		# image
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

			# display corner mask
			cv2.imshow("Corner Mask",cornerMask)
			key=cv2.waitKey(0)

			# extract HSV masked corner image
			masked=cv2.bitwise_and(image,image,mask=cornerMask)

			# display HSV masked corner image
			cv2.imshow("Masked Corner Image",masked)
			key=cv2.waitKey(0)

		# extract a color histogram from the elliptical region
		cv2.imshow("Ellipse Mask",ellipMask)
		key=cv2.waitKey(0)

		# extract HSV masked elliptical image
		masked=cv2.bitwise_and(image,image,mask=ellipMask)

		# display HSV masked elliptical image
		cv2.imshow("Maked Elliptical Mask",masked)
		key=cv2.waitKey(0)

# using ColorDescriptor class, describe the image descriptor (3D HSV Color Model)
# and read an image to mask and plot
image=cv2.imread("101401.png")
ColorDescriptor((8,12,3)).describe(image)