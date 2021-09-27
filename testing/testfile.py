import os 

files = os.listdir('testing/originals/')
original_path = 'testing/originals'
for file in files:
    new_path = 'testing/copied'
    filepath = os.path.join(original_path, file)
    with open(filepath, 'r') as f:
        lines = f.read()
    new_path = os.path.join(new_path, file)
    with open(new_path, 'w') as f1:
        f1.write(lines)
        

    