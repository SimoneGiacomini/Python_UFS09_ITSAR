"""Creare un programma che permetta all’utente di effettuare la divisione tra due numeri
e mostri a schermo quoziente e resto senza utilizzare né l’operatore / né l’operatore %"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma permette di fare la divisione (intera) tra 2 numeri usando una funzione la quale NON 
utilizza l'operatore "/" e "%"
"""

#------------FUNZIONI----------------
##funzione che effettua la divisione utilizzando solo la sottrazione
#ritorna None se la divisione è impossibile
#un numero reale invece se tutto va a buon fine (quoziente)
def myDivision(dividendo, divisore):
    segno=1
    #divisione impossibile:
    if divisore == 0:
        return None
    #quoziente sicuramente uguale a 0
    if dividendo == 0 :
        return 0

    #check del segno
    if dividendo<0:
        dividendo=dividendo*-1
        segno= segno*-1
    if divisore<0:
        divisore=divisore*-1
        segno=  segno*-1
    
    quoziente =0
    while (dividendo-divisore)>=0:
        quoziente+=1
        dividendo= dividendo-divisore
    return quoziente *segno
##funzione che calcola il resto di una divisione  senza "%"
#ritorna None se non è possibile calcolarlo (divisore uguale a 0)
#un numero reale invece se tutto va a buon fine
def myResto(dividendo, divisore):
    #divisione impossibile:
    segno =1
    if divisore == 0:
        return None
    #resto uguale a divisore
    if dividendo == 0 :
        return divisore
    
    #check del segno
    if dividendo<0:
        dividendo=dividendo*-1
        #segno= segno*-1
    if divisore<0:
        divisore=divisore*-1
        #segno=  segno*-1
    
    while (dividendo-divisore)>=0:
        dividendo= dividendo-divisore
    return dividendo

##Funzione che utilizza le eccezioni trovata su stack overflow
#ritorna vero se il valore passato può essere convertito in un numero reale
#falso altrimenti
def isNumber(numero):
    try:
        float(numero)
        return True
    except:
        return False
#------------FINE FUNZIONI----------------


#inizio programma
print(SALUTO)

dividendo = input("Inserisci il dividendo : ")
while not isNumber(dividendo):
    print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")
    dividendo = input("Inserisci il dividendo : ")
    
dividendo=float(dividendo)

divisore = input("Inserisci il divisore : ")
while not isNumber(divisore):
    print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")
    divisore = input("Inserisci il divisore : ")
    
divisore=float(divisore)

quoz= myDivision(dividendo,divisore)
resto= myResto(dividendo,divisore)
if quoz== None or resto == None:
    print("Impossibile calcolare nè il resto nè la divisione")
else:
    print("\nLa divisione tra {} e {} è uguale a {}\nMentre il resto è {}".format(dividendo,divisore, quoz, resto))
