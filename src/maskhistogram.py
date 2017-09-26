# Import the necessary packages
# maskhistogram.py displays 2D plots of Hue and Saturation of query image
# and result images which are similar or dissmimilar to the query image
# Folder 'pics' contains similar images
# Folder 'non' contains dissimilar images
# maskhistogram.py is a demo class to explain how color histograms of
# images can be compared to find out similar images
# Demo class

import cv2
from matplotlib import pyplot as plt
import os

class ColorDescriptor:

	def __init__(self, bins):

		# store the number of bins for the 3D histogram
		self.bins = bins

	def describe(self):

		# 'pics' folder contains 123602.png, 123800.png, 124001.png (Similar pictures)
		# 'non' folder contains 123602.png, 123800.png, 13.png (Dissimilar pictures)
		t=['pics','non']

		# Looping for each folder
		for item in t:

			# Path to the folders
			mypath=os.path.join('C:\\','Users','arpita','PycharmProjects','Project','src',item)
			images=list()

			# hist list stores calculated histogram of parsed images in a folder
			hist=[]

			# imageid list stores the image ID's of parsed images in a folder
			imageid=[]

			# Looping for each image in a folder
			for item in os.listdir(mypath):
				image=cv2.imread(os.path.join(mypath,item))

				# Convert the image to the HSV color space
				image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

				# Store the imageID of image in a list
				imageid.append(item)

				# Calculate 2D Histogram of 3D HSV image and store it in a list
				hist.append(cv2.calcHist([image], [0, 1], None, [180,256],[0, 180, 0, 256]))

			# i represents position of subplot in the main plot
			i=321

			# Loop over each image in a folder using items in list 'imageID'
			# Create subplots of images in main plot
			# Each row contains and image and its histogram
			for item in imageid:

				# Print the Image ID on console
				print item
				im=cv2.imread(os.path.join(mypath,item))

				# 123602.png is query image
				if item=="123602.png":
					cv2.imshow(item,im)

					# Create subplot with title 'QUERY IMAGE'
					plt.subplot(i), plt.imshow(im), plt.title("Query Image")

				else:
					cv2.imshow(item,im)

					# Create subplot with title 'RESULT IMAGE'
					plt.subplot(i), plt.imshow(im), plt.title("Result Image")

				# To place subploot in the next row
				i=i+2

			i=322

			# Loop over items in list hist and plot them next to the
			# corresponding image in each row
			for item in hist:
				plt.subplot(i),plt.imshow(item)
				i=i+2
			plt.title("Plot"),plt.show()


# using ColorDescriptor class, describe the image descriptor (3D HSV Color Model)
ColorDescriptor((8,12,3)).describe()