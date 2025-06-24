name = input("Comment tu t'appel ? ")

print("En majuscule :", name.upper())
print("En minuscule:", name.lower())

Taille = len(name.replace(" ", ""))
print("Nombre de lettres : ", Taille)