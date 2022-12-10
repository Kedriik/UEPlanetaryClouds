import cv2
import json
import math
from PIL import Image

def clip(value, lower, upper):
    return lower if value < lower else upper if value > upper else value

def linear_func(a,x,b):
    return a*x+b
cloud_image = Image.open('imagedata\clouds.jpg')
for x in range(cloud_image.width):
    for y in range(cloud_image.height):
        current_val = cloud_image.getpixel((x,y))[0]
        cloud_image.putpixel((x,y), 
                             (clip(int(linear_func(2,current_val,0)),0,255),
                              50+clip(int(linear_func(0,current_val,-450)),0,255),0) )
       # if current_val < int(255/2):
        #    cloud_image.putpixel( (x,y), (2*current_val,0,0))
       # else:
       #     cloud_image.putpixel( (x,y), (255,int(1*(current_val-128)),0) )

width, height = cloud_image.size
new_width = width*10
concat = int(new_width/float(cloud_image.size[0]))
size = int((float(cloud_image.size[1])*float(concat)))
resized_im = cloud_image.resize((new_width,size), Image.ANTIALIAS)

#for x in range(resized_im.width):
#    for y in range(resized_im.height):
#        current_val = (resized_im.getpixel((x,y))[0]+resized_im.getpixel((x,y))[1])/2
#        
#        if current_val < 100:
#            resized_im.putpixel( (x,y), (0,0,0))
            
resized_im.save('imagedata\cloudsUE.jpg')

#y = a*x+b