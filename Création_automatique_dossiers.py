import os 

for i in range(1, 6):
    folder = f"Projet{i}"
    if not os.path.exists(folder):
        os.mkdir(folder)