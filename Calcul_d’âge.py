annee_naissance = int(input("Quelle est ton année de naissance ? "))
age = 2025 - annee_naissance

print("Tu as", age, "ans.")

if age >= 18:
    print("Tu es majeur")
else:
    print("tu es mineur")