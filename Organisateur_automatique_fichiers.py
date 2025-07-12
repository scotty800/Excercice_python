import os
import shutil

types = {
    ".txt": "Textes",
    ".pdf": "Documents",
    ".jpg": "Images",
    ".png": "Images"
}

for f in os.listdir("inbox"):
    chemin = os.path.join("inbox", f)
    if os.path.isfile(chemin):
        ext = os.path.splitext(f)[1].lower()
        dossier = types.get(ext)
        if dossier:
            dest = os.path.join("inbox", dossier)
            os.makedirs(dest, exist_ok=True)
            shutil.move(chemin, os.path.join(dest, f))
            print(f"{f} → {dossier}/")
        else:
            print(f"{f} ignoré (extension non prise en charge)")

print("\nOrganisation terminée.")
