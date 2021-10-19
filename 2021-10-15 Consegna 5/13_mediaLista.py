"""Scrivere una funzione che restituisce la media dei numeri passati come lista"""


#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input una lista di numeri e ritorna la loro media"
"""

#ritorna la media dei numeri di un lista passata
def mediaDiLista(lista):
    somma=0
    for e in lista:
        somma+=e
    if len(lista)==0:
        return None
    return somma/len(lista)

##funzione che crea una lista
#viene creata una lista dinamica chiedendo dopo ogni inserimento se si vuole concludere oppure andare avanti nell'inserire elementi nella lista
#la funzione riesce a distinguere se gli elementi inseriti sono numeri o stringhe
def creaLista():
    lista=[]
    contatore=0
    while True:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if isNumber(elem)  :
            num=float(elem)
            lista.append(num)
        else :
            print("\nL'Input inserito non è un numero")
            contatore-=1 #si sottrae in quanto non è un input soddisfacente, ciclo sfalsato
        scelta=input("""\nVuoi inserire un nuovo elemento? \nNo -> 0\nSi -> qualsiasi altro tasto\n--> """)
        if scelta.find("0") == 0:
            return lista
        contatore+=1

##Funzione che utilizza le eccezioni trovata su stack overflow, se è un numero ritorna vero
#altrimenti falso
def isNumber(numero):
    try:
        float(numero)
        return True
    except:
        return False


#inizio programma
print(SALUTO)
lista=creaLista()
ris=mediaDiLista(lista)
if ris == None:
    print("\nLa lista è vuota, impossibile calcolare una media\n")
else:
    print("la media dei numeri {} è di {}".format(lista,ris))