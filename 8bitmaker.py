import os
from PIL import Image
import cv2


original_path = 'original_images'
new_path = 'converted_images'
files = os.listdir(original_path)
for file in files:
    new_name = file.split('.')
    new_name = new_name[0] + '.png'
    image_path = os.path.join(original_path, file)
    new_path = os.path.join(new_path, new_name)
    image = Image.open(image_path)
    image.save(new_path)
    

    


