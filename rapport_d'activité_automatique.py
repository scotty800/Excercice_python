import os
import shutil
from datetime import datetime

def ecrire_rapport(chemin_dossier, action, fichiers):
    with open("rapport.txt", "a", encoding="utf-8") as f:
        date = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{date} {action} dans dossier : {chemin_dossier}\n")
        if fichiers:
            f.write(f"Fichiers concernés ({len(fichiers)}) :\n")
            for fichier in fichiers:
                f.write(f"- {fichier}\n")
        else:
            f.write("Aucun fichier traité.\n")
        f.write("\n")

def nettoyer_dossier(chemin_dossier):
    temp_ext = [".tmp", ".bak", ".log"]
    fichiers_supprimes = []

    for f in os.listdir(chemin_dossier):
        chemin = os.path.join(chemin_dossier, f)
        if os.path.isfile(chemin):
            ext = os.path.splitext(f)[1].lower()
            if os.path.getsize(chemin) == 0 or ext in temp_ext:
                corbeille = os.path.join(chemin_dossier, ".corbeille_temp")
                os.makedirs(corbeille, exist_ok=True)
                shutil.move(chemin, os.path.join(corbeille, f))
                fichiers_supprimes.append(f)
                print(f"Supprimé : {f}")

    print(f"\nTotal de fichiers supprimés : {len(fichiers_supprimes)}")
    ecrire_rapport(chemin_dossier, "Nettoyage", fichiers_supprimes)

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

    fichiers_deplaces = []
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
                fichiers_deplaces.append(f)
            else:
                ignores += 1

    print("\nRésumé :")
    print(f"Fichiers déplacés : {len(fichiers_deplaces)}")
    print(f"Fichiers ignorés  : {ignores}")
    ecrire_rapport(chemin_dossier, "Organisation", fichiers_deplaces)

def restaurer_fichier(chemin):
    corbeille = os.path.join(chemin, ".corbeille_temp")
    if not os.path.isdir(corbeille):
        print("Aucune corbeille trouvée.")
        return
    
    fichiers = [f for f in os.listdir(corbeille) if os.path.isfile(os.path.join(corbeille, f))]
    if not fichiers:
        print("La corbeille est vide.")
        return
    
    print("Fichiers dans la corbeille :")
    for i, f in enumerate(fichiers, 1):
        print(f"{i}. {f}")
    
    try:
        choix = int(input("Quel fichier restaurer ? (numéro) : "))
        if 1 <= choix <= len(fichiers):
            fichier = fichiers[choix - 1]
            shutil.move(os.path.join(corbeille, fichier), os.path.join(chemin, fichier))
            print(f"Fichier restauré : {fichier}")
            ecrire_rapport(chemin, "Restauration", [fichier])
        else:
            print("Choix invalide.")
    except ValueError:
        print("Entrée non valide.")

def afficher_menu():
    print("\n=== Outil de maintenance ===")
    print("1. Nettoyer les fichiers temporaires")
    print("2. Organiser les fichiers par type")
    print("3. Restaurer un fichier supprimé")
    print("4. Quitter")

while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        chemin = input("Chemin du dossier à nettoyer : ")
        if os.path.isdir(chemin):
            nettoyer_dossier(chemin)
        else:
            print("Dossier invalide.")
    elif choix == "2":
        chemin = input("Chemin du dossier à organiser : ")
        if os.path.isdir(chemin):
            organiser_dossier(chemin)
        else:
            print("Dossier invalide.")
    elif choix == "3":
        chemin = input("Chemin du dossier avec corbeille : ")
        if os.path.isdir(chemin):
            restaurer_fichier(chemin)
        else:
            print("Dossier invalide.")
    elif choix == "4":
        print("À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
