import os

for i in range(1, 6):
    folder = f"Projet{i}"
    if not os.path.exists(folder):
        os.mkdir(folder)
        
    Fichier = os.path.join(folder, "README.txt")
    
    contenu = f"Ceci est le dossier Projet{i}"
    
    with open(Fichier, "w") as f:
        f.write(contenu)