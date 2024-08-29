somme_paire=0
r=int(input("ecrivez un nombre positif : "))

for n in range(1,r+1):
    if n % 2 ==0 :
        somme_paire += n
print(f"somme de 1 a {r} est {somme_paire} ")


n = 0
somme_paire = 0  # Variable pour stocker la somme des nombres pairs
r = int(input("Écrivez un nombre entier positif : "))

while n <= r:
    if n % 2 == 0:  # Vérification si le nombre est pair
        somme_paire += n  # Ajout du nombre pair à la somme
        # ou somme_paire = somme_paire + 1

    n += 1  # Incrémenter n à chaque itération

print(f"La somme des nombres pairs de 1 à {r} est : {somme_paire}")


def somme_nombres_pairs(n):
    somme = 0  # Variable pour stocker la somme des nombres pairs
    for i in range(1, n + 1):  # Parcours des nombres de 1 à n
        if i % 2 == 0:  # Vérification si le nombre est pair
            somme += i  # Ajout du nombre pair à la somme
    return somme

# Programme principal
try:
    n = int(input("Entrez un nombre entier positif : "))
    if n < 0:
        print("Veuillez entrer un nombre entier positif.")
    else:
        resultat = somme_nombres_pairs(n)
        print(f"La somme des nombres pairs de 1 à {n} est : {resultat}")
except ValueError:
    print("Veuillez entrer un nombre valide.")