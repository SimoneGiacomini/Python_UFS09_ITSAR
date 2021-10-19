"""Creare un programma che permetta all’utente di effettuare la moltiplicazione tra due
numeri senza utilizzare l’operatore * ma calcolando il risultato attraverso somme
ripetute (numeri positivi)."""

##Funzione che fa la moltiplicazione tra 2 numeri usando la somma
def myMoltiplication(num1, num2):
    somma=0
    for e in range(0,num2):
        somma=somma+num1
    return somma


print("""CIAO ~Simone Giacomini
Questo programma permette di fare la moltiplicazione tra 2 numeri interi usando una funzione la quale utilizza solo la somma 
""")
moltiplicatore = "None"
moltiplicando = moltiplicatore
while not moltiplicando.isnumeric():
    moltiplicando = input("Inserisci il moltiplicando (1° fattore): ")
    
    if moltiplicando.isnumeric():
       break
    else:
        print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")

moltiplicando=int(moltiplicando)

while not moltiplicatore.isnumeric():
    moltiplicatore = input("Inserisci il moltiplicatore (2° fattore): ")
    
    if moltiplicatore.isnumeric():
        break
    else:
        print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")
moltiplicatore=int(moltiplicatore)
print("\nLa moltiplicazione tra {} e {} è uguale a {}".format(moltiplicando,moltiplicatore, myMoltiplication(moltiplicando, moltiplicatore)))