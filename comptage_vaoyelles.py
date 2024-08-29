voyelle=["a", "e", "i","o", "u", "A", "E", "I", "O", "U"]

chaine = input("ecrire une chaine de caractère : ")
compteur_voyelles = 0

for char in chaine:
    if char in voyelle:
        compteur_voyelles += 1
        print(char)

print(f"Le nombre total de voyelles est : {compteur_voyelles}")


voyelles="a, e, i, o, u, A, E, I, O, U)"
chaine2 = input("ecrire une chaine de caractère 2 : ")
compteur_voyelle2 = 0
# Boucle pour parcourir chaque caractère de la chaîne
for chary in chaine2:
    if chary in voyelles:  # Vérification si le caractère est une voyelle
        compteur_voyelle2 += 1  # Incrémentation du compteur de voyelles
        print(chary)

# Affichage du résultat
print(f"Le nombre total de voyelles est : {compteur_voyelle2}")