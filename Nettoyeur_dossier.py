import os

temporaires_ext = [".tmp", ".bak", ".log"]

chemin_dossier = input("Le chemin du dossier à nettoyer : ")

supprime = 0

for f in os.listdir(chemin_dossier):
    chemin = os.path.join(chemin_dossier, f)
    if os.path.isfile(chemin):
        ext = os.path.splitext(f)[1].lower()
        if os.path.getsize(chemin) == 0 or ext in temporaires_ext:
            os.remove(chemin)
            supprime += 1
            print(f"Supprimé : {f}")

print(f"\nTotal de fichiers supprimés : {supprime}")
