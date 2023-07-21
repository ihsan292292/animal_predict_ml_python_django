import os
import cv2
from PIL import Image 
import numpy as np

data = []
labels = []

# cat 0
cats = os.listdir(os.getcwd() + "/CNN/data/cat/")
for x in cats:
    """
    loop through all images in the directory 
    1.convert to arrays 
    2.Resize the images 
    3.Add images to dataset 
    4.Add the labels 
    """
    img = cv2.imread(os.getcwd()+"/CNN/data/cat/" + x)
    img_from_ar = Image.fromarray(img,'RGB')
    resized_image = img_from_ar.resize((50,50))
    data.append(np.array(resized_image))
    labels.append(0)
    
    
# Dog 1
dogs = os.listdir(os.getcwd() + "/CNN/data/Dog/")
for x in dogs:
    imag=cv2.imread(os.getcwd() + "/CNN/data/Dog/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)
    
# Monkey 2
monkeys = os.listdir(os.getcwd() + "/CNN/data/Monkey/")
for x in monkeys:
    imag=cv2.imread(os.getcwd() + "/CNN/data/Monkey/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)
    
# Parrot 3
parrots = os.listdir(os.getcwd() + "/CNN/data/Parrot/")
for x in parrots:
    imag=cv2.imread(os.getcwd() + "/CNN/data/Parrot/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)
    
# Elephant 4
elephants = os.listdir(os.getcwd() + "/CNN/data/Elephant/")
for x in elephants:
    imag=cv2.imread(os.getcwd() + "/CNN/data/Elephant/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)
    
# Bear 5
bears = os.listdir(os.getcwd() + "/CNN/data/bear/")
for x in bears:
    imag=cv2.imread(os.getcwd() + "/CNN/data/bear/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(5)

    
#load the animals and the labels 
animals = np.array(data) 
labels = np.array(labels)

#save 
np.save("animals",animals)
np.save("labels",labels)
