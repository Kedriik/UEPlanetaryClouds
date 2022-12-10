import cv2
import json
import math
from PIL import Image,ImageFilter
cloud_image = Image.open('imagedata\KindOfClouds.jpg')

width, height = cloud_image.size
new_width = width*10
concat = int(new_width/float(cloud_image.size[0]))
size = int((float(cloud_image.size[1])*float(concat)))
resized_im = cloud_image.resize((new_width,size), Image.ANTIALIAS)
for i in range(1,10):
    resized_im = resized_im.filter(ImageFilter.BoxBlur(5*i))

for i in range(1,10):
    resized_im = resized_im.filter(ImageFilter.BoxBlur(2*i))

for i in range(1,10):
    resized_im = resized_im.filter(ImageFilter.BoxBlur(5*i))
            
resized_im.save('imagedata\KindOfCloudsUE.jpg')