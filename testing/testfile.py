import os 

files = os.listdir('testing/originals/')
original_path = 'testing/originals'
for file in files:
    filepath = os.path.join(original_path, file)
    print(filepath) 