
def fonction() :
  N = int(input("Entrez un nombre entre 1 et 3: "))
  
  
  while N < 1 or N > 3:
      if N < 1 or N > 3:
          print("Saisie erronée. Recommencez")
          N = int(input("Entrez un nombre entre 1 et 3 encore une fois : "))
  print("correct")

