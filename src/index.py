
# import the necessary packages
from colordescriptor import ColorDescriptor
import cv2
import os

mypath=os.path.join('C:\\','Users','arpita','PycharmProjects','Project','src','dataset')
images=list()
indexpath=os.path.join('C:\\','Users','arpita','PycharmProjects','Project','src','index.csv')

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output=open("index.csv",mode="w")

for item in os.listdir(mypath):
    image=cv2.imread(os.path.join(mypath,item))
    imageID=item
    features = cd.describe(image)

    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()