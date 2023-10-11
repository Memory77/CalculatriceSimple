from addition import addition

from soustraction import soustraction

from division import division

from multiplication import multiplication

chiffre_1 = float(input("Tapez le premier chiffre :"))
operation = input("Sélectionner votre opération")
chiffre_2 = float(input("Tapez le deuxième chiffre : "))


def calculatrice (a, b, c):
        if b == "addition" or b == "+":
            resultat = addition(a, c)
            resultat = round(resultat, 2)
            return resultat
        
        elif b == "soustraction" or b == "-":
              resultat = soustraction(a, c)
              resultat = round(resultat, 2)
              return resultat
        
        elif b == "division" or b == "/":
              resultat = division(a, c)
              resultat = round(resultat, 2)
              return resultat
        
        elif b == "multiplication" or b == "*":
              resultat = multiplication(a, c)
              resultat = round(resultat, 2)
              return resultat
        else:
              print("Opération invalide")

print(calculatrice(chiffre_1, operation, chiffre_2,))




