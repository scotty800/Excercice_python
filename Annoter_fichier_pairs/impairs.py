with open("rapport.txt", "w") as rapport:
    for i in range(1, 6):
        nom_fichier = f"fiche{i}.txt"
        with open(nom_fichier, "r") as fichier:
            contenu = fichier.read()
            annotation = "(Fichier pair)" if i % 2 == 0 else "(Fichier impair)"
            
            print(f"Contenu de {nom_fichier} : {annotation} \n{contenu}\n")
            rapport.write(f"--- {nom_fichier} --- {annotation}\n{contenu}\n\n")
