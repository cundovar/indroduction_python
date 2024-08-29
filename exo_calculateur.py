


def calculer_moyenne(notes):
    if len(notes)==0 :
        return 0
    #calcule moyenne : somme des notes et longueur de notes
    return sum(notes)/len(notes)

def saisir_notes():
    notes=[]
    while True:
        try:
            note=float(input("entrez une note ou un nombre négatif pour finir la liste : "))
            if note < 0:
                break
            notes.append(note)
        except ValueError:
            print("saisir un nombre !!!")

    return notes
    
def afficher_moyenne(moyenne):
    print(f"la moyenne est : {round(moyenne,2)}")


#programe principale les fonctions sont appellé
notes=saisir_notes()
moyenne=calculer_moyenne(notes)
afficher_moyenne(moyenne)


