import os 
from PIL import Image

converted_path = 'converted_images'
new_path = 'stripped'
files = os.listdir(converted_path)
for file in files:
    path = os.path.join(converted_path, file)
    new_pathname = os.path.join(new_path, file)
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(new_pathname)
    print('Done')
