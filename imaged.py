#!/usr/bin/env python3

from PIL import Image
from os import listdir
import os

img_dir ="./images"

for image in os.listdir(img_dir):
    image_name, ext = os.path.splitext(image)
    im=Image.open("./images/"+image)
    im= im.rotate(360-90).resize((128,128))
    if im.mode != 'RGB':
    	im = im.convert('RGB')
    im.save("/opt/icons/" + image_name + ".jpeg", "JPEG")


