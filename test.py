
# Demander à l'utilisateur d'entrer deux nombres
nombre1 = int(input("Entrez le premier nombre: "))
nombre2 = int(input("Entrez le deuxième nombre: "))

# Calculer la somme des deux nombres
somme = nombre1 + nombre2

# Calculer le produit des deux nombres
produit = nombre1 * nombre2

# Afficher les résultats
print(f"La somme de {nombre1} et {nombre2} est: {somme}")
print(f"Le produit de {nombre1} et {nombre2} est: {produit}")


n1=float(input("1er nombre : "))
n2=float(input("2eme nombre : "))
n3=float(input("3eme nombre : "))
_n=[n1,n2,n3]
n=sum(_n)
#convertire en chaine de caratètère le round
print( "resulat : "+str(round(+n,2)))