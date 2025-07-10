Moyennes = []

with open("bilan.txt", "w") as rapport:
    for i in range(1, 6):
        nom_fichier = f"eleve{i}.txt"
        with open(nom_fichier, "r") as fichier:
            contenu = fichier.read()
            notes = list(map(int, contenu.split()))
            
            moyenne = sum(notes) / len(notes)
            maximum = max(notes)
            minimum = min(notes)
            
            Moyennes.append(moyenne)
            rapport.write(f"Élève {i} -> Moyenne: {moyenne:.2f} | Max: {maximum} | Min: {minimum}\n")
            
    moyenne_classe = sum(Moyennes) / len(Moyennes)
    rapport.write(f"Moyenne général de la classe : {moyenne_classe:.2f}\n")
            