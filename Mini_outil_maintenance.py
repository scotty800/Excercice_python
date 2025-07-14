import os
import shutil

def nettoyer_dossier(chemin_dossier):
    temp_ext = [".tmp", ".bak", ".log"]
    sup = 0

    for f in os.listdir(chemin_dossier):
        chemin = os.path.join(chemin_dossier, f)
        if os.path.isfile(chemin):
            ext = os.path.splitext(f)[1].lower()
            if os.path.getsize(chemin) == 0 or ext in temp_ext:
                os.remove(chemin)
                sup += 1
                print(f"Supprimé : {f}")

    print(f"\nTotal de fichiers supprimés : {sup}")

def organiser_dossier(chemin_dossier):
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

def afficher_menu():
    print("\n=== Outil de maintenance ===")
    print("1. Nettoyer les fichiers temporaires")
    print("2. Organiser les fichiers par type")
    print("3. Quitter")

while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        chemin = input("Chemin du dossier à nettoyer : ")
        nettoyer_dossier(chemin)
    elif choix == "2":
        chemin = input("Chemin du dossier à organiser : ")
        organiser_dossier(chemin)
    elif choix == "3":
        print("À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
