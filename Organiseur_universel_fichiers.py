import os
import shutil

chemin_dossier = input("Le chemin d'un dossier à organiser : ")

types = {
    ".txt": "Textes",
    ".md": "Textes",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Vidéos",
    ".avi": "Vidéos",
    ".pdf": "Documents",
    ".docx": "Documents"
}

deplace = 0
ignores = 0

for f in os.listdir(chemin_dossier):
    chemin = os.path.join(chemin_dossier, f)
    if os.path.isfile(chemin):
        ext = os.path.splitext(f)[1].lower()
        dossier = types.get(ext)
        if dossier:
            dest = os.path.join(chemin_dossier, dossier)
            os.makedirs(dest, exist_ok=True)
            shutil.move(chemin, os.path.join(dest, f))
            print(f"{f} → {dossier}/")
            deplace += 1
        else:
            ignores += 1

print("\nRésumé :")
print(f"Fichiers déplacés : {deplace}")
print(f"Fichiers ignorés  : {ignores}")
