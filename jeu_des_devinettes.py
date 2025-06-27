mot_secret = "java"
essaie = 0
deviner = ""

while deviner != mot_secret:
    deviner = input("Devine le mot secret : ").lower().strip()
    essaie += 1
    if deviner != mot_secret:
        print("Raté, essaie encore.")

print("Bravo, tu as trouvé en", essaie, "essai(s) !")
