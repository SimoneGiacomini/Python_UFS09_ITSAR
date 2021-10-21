"""Creare una funzione che, data una lista di numeri ed un numero da cercare,
restituisca il valore booleano True se tale numero è presente nella lista, False
altrimenti"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input una lista di numeri ed infine un numero da cercare, se quel numero è presente nella lista ti fa un complimento"
"""

##Funzione che utilizza le eccezioni trovata su stack overflow
#ritorna vero se il valore passato può essere convertito in un numero reale
#falso altrimenti
def isNumber(numero):
    try:
        float(numero)
        return True
    except:
        return False

#funzione richiesta dall'esercizio
def isInLista(lista, valore_da_cercare):
    if valore_da_cercare in lista:
        return True 
    else:
        return False 

##funzione che crea una lista con anche i float
#viene creata una lista dinamica chiedendo dopo ogni inserimento se si vuole concludere oppure andare avanti nell'inserire elementi nella lista
#la funzione riesce a distinguere se gli elementi inseriti sono numeri o stringhe
def creaLista():
    lista=[]
    contatore=0
    while 1==1:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if isNumber(elem)  :
            lista.append(float(elem))
        else :
            print("\nL'Input inserito non è un numero")
            contatore-=1 #si sottrae in quanto non è un input soddisfacente, ciclo sfalsato
        scelta=input("""\nVuoi inserire un nuovo elemento? \nNo -> 0\nSi -> qualsiasi altro tasto\n--> """)
        if scelta.find("0") == 0:
            return lista
        contatore+=1

#inizio programma
print(SALUTO)
lista = creaLista()
print("La lista creata è:\n{}".format(lista))
numero_da_cercare= input("Inserisci ora il numero da cercare: ")
while not isNumber(numero_da_cercare):
    numero_da_cercare= input("Il valore che hai inserito non è un numero\nriprova: ")
numero_da_cercare=float(numero_da_cercare)
if isInLista(lista, numero_da_cercare):
    print("Complimenti =)\nil valore {} è presente nella lista {}".format(numero_da_cercare, lista))
else:
    print("Sfortunatamente =(\nil valore {} NON è presente nella lista {}".format(numero_da_cercare, lista))