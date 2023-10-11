from addition import addition

from soustraction import soustraction

from division import division

from multiplication import multiplication

ch_1 = float(input("Tapez le premier chiffre :"))
ope = input("Sélectionner votre opération")
ch_2 = float(input("Tapez le deuxième chiffre : "))


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

print(calculatrice(ch_1, ope, ch_2,))


custom_result = (calculatrice(ch_1, ope, ch_2))
custom = f""""
 _____________________
|  _________________  |
| | {ch_1} {ope} {ch_2}  
 
    = {custom_result}
    

| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

    """
print(custom)




