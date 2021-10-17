#Implementare una calcolatrice chiedendo all’utente di inserire i valori e l’operatore
print("""CIAO ~Simone Giacomini
Questo programma chiede in input 2 numeri ed un operatore e fa da calcolatrice\n""")

operatori = "+-*/:^"

numero1= int(input("Inserisci il primo numero: "))
numero2= int(input("Inserisci il secondo numero: "))
operatore = input("inserisci l'operatore \n somma(+),\n sottrazione(-),\n moltiplicazione(*),\n divisione(/ oppure :),\n elevazione(^)\n--> ")
#,\n percentuale(%)
while operatore not in operatori or len(operatore)>1 :
    operatore = input("Reinserisci l'operatore, quello che hai inserito non esiste: ")
if operatore == "+" :
    print ("\nhai scelto somma\nIl risultato è "+str(numero1+numero2))
elif operatore == "-" :
    print ("\nhai scelto differenza\nIl risultato è "+str(numero1-numero2))
elif operatore == "*" :
    print ("\nhai scelto moltiplicazione\nIl risultato è "+str(numero1*numero2))
elif operatore == "/" or operatore == ":" :
    print ("\nhai scelto divisione\n")
    if numero2 == 0:
        print("Il risultato è impossibile")
    else :
        print("Il risultato è "+str(numero1/numero2))
elif operatore == "^" :
    print ("\nhai scelto elevazione\nIl risultato è "+str(numero1**numero2))
else :
    print("problema")

          