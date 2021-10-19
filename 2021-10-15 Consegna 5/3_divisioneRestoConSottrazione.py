"""Creare un programma che permetta all’utente di effettuare la divisione tra due numeri
e mostri a schermo quoziente e resto senza utilizzare né l’operatore / né l’operatore %"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma permette di fare la divisione (intera) tra 2 numeri interi usando una funzione la quale NON 
utilizza l'operatore "/" e "%"
"""

#------------FUNZIONI----------------
##funzione che effettua la divisione utilizzando solo la sottrazione
#ritorna None se la divisione è impossibile
#un numero intero invece se tutto va a buon fine (quoziente)
def myDivision(dividendo, divisore):
    #divisione impossibile:
    if divisore == 0:
        return None
    #quoziente sicuramente uguale a 0
    if dividendo == 0 :
        return 0
    quoziente =0
    while (dividendo-divisore)>=0:
        quoziente+=1
        dividendo= dividendo-divisore
    return quoziente
##funzione che calcola il resto di una divisione intera senza "%"
#ritorna None se non è possibile calcolarlo (divisore uguale a 0)
#un numero intero invece se tutto va a buon fine
def myResto(dividendo, divisore):
    #divisione impossibile:
    if divisore == 0:
        return None
    #resto uguale a divisore
    if dividendo == 0 :
        return divisore
    while (dividendo-divisore)>=0:
        dividendo= dividendo-divisore
    return dividendo
#------------FINE FUNZIONI----------------


#inizio programma
print(SALUTO)

divisore = "None"
dividendo = divisore
while not dividendo.isnumeric():
    dividendo = input("Inserisci il dividendo : ")
    
    if dividendo.isnumeric():
       break
    else:
        print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")

dividendo=int(dividendo)

while not divisore.isnumeric():
    divisore = input("Inserisci il divisore: ")
    
    if divisore.isnumeric():
        break
    else:
        print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")
divisore=int(divisore)
quoz= myDivision(dividendo,divisore)
resto= myResto(dividendo,divisore)
if quoz== None or resto == None:
    print("Impossibile calcolare nè il resto nè la divisione")
else:
    print("\nLa divisione tra {} e {} è uguale a {}\nMentre il resto è {}".format(dividendo,divisore, quoz, resto))
