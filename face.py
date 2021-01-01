import os
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
image_dir = os.path.join(BASE_DIR, "emotional_recognition/data")
#print(image_dir)

emotions = ["angry", "disgust","fear", "happy", "neutral","sad","surprise"]


for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg"):
            path = os.path.join(root,file)
            
            label = os.path.basename(root).replace(" ","-").lower()
            print(label)
            print(path)
            im = Image.open(path)
            w,h = im.size
            im1 = im.crop((0,0,w,h/2))
            im2 = im.crop((0,h/2,w,h))
            #im1.save( root + "/upper_" + file,"JPEG")
            im2.save( root + "/lower_" + file,"JPEG")
            # im1.save(os.path.join(root, "upper",'JPEG'))
            # im2.save(os.path.join(root, "lower",'JPEG'))

