import os

i = 1

for nom in os.listdir("docs"):
    if nom.endswith(".txt"):
        ancien = os.path.join("docs", nom)
        nouveau = os.path.join("docs", f"document{i}.txt")
        os.rename(ancien, nouveau)
        print(f"{nom} ->  document_{i}.txt")
        i += 1