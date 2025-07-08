with open("bilan.txt", "w") as rapport:
    for i in range(1, 6):
        nom_fichier = f"eleve{i}.txt"
        with open(nom_fichier, "r") as fichier:
            contenu = fichier.read()
            notes = list(map(int, contenu.split()))
            moyenne = sum(notes) / len(notes)
            notes_max = max(notes)
            notes_min = min(notes)
            print(f"Eleve {i} -> Moyenne: {moyenne:.2f} | Max: {notes_max} | Min: {notes_min}")
            rapport.write(f"Eleve {i} -> Moyenne: {moyenne:.2f} | Max: {notes_max} | Min: {notes_min}\n")