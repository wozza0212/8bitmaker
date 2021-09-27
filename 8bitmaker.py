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
    picture = cv2.imread(new_path)
    height, width = picture.shape[:2]
    w, h = (256, 256)
    temp = cv2.resize(picture, (w, h), interpolation = cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(new_path, output)