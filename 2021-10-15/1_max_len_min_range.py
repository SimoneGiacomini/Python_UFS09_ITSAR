"""Implementare delle funzioni che consentano di trovare il massimo, minimo, contare il
numero di elementi su una lista e ridefinire la funzione range senza usare le funzioni
predefinite di python (len, max, min, range)."""


#Menu che viene visualizzato ad ogni interazione
MENU= """MENU
1-> len di una lista
2-> max di una lista
3-> min di una lista
4-> range di due valori
0-> Esci dal menù
-> """

#Stringa che segnala un problema con i valori inseriti
PROBLEMA="\n-------------------------------\nC'è un PROBLEMA con la lista che hai inserito\n-------------------------------\n"

#Frase che viene usata quando si utilizza il metodo creaLista()
CREALISTA="Creiamo una lista allora!"

"""Funzione myMax
#@input una lista di numeri, se ci sono stringhe le scarta
#@return il numero maggiore all'interno di una lista
"""
def myMax(lista):
    lista_sup=[] #lista supplementare per controllare se ci sono dei numeri nella lista inserita
    if isinstance( lista,list): #check per controllare se il valore passato è una lista
        for elem in lista :  #for su lista per cercare gli elementi che sono numeri
           if isinstance(elem, int): #
               lista_sup.append(elem)

        if myLen(lista_sup)==0:# se tutti gli elementi nella lista originale sono stringhe allora ritorno None per dire che c'è un problema
            return None
        massimo=lista_sup[0] # prendo per assoluto che il primo elemento sia il maggiore
        for elem in lista_sup  :
            if elem>massimo: #elemento fondamentale
                massimo=elem #scambio
        return massimo
    else:
        return None #se non è una lista ritorno None per far capire che c'è un problema


## Funzione myMin
#@input una lista di numeri, se ci sono stringhe le scarta
#@return il numero MINORE all'interno di una lista
def myMin(lista):
    lista_sup=[] #lista supplementare per controllare se ci sono dei numeri nella lista inserita
    if isinstance( lista,list): #check per controllare se il valore passato è una lista
        for elem in lista :  #for su lista per cercare gli elementi che sono numeri
           if isinstance(elem, int): #
               lista_sup.append(elem)

        if myLen(lista_sup)==0:# se tutti gli elementi nella lista originale sono stringhe allora ritorno None per dire che c'è un problema
            return None
        massimo=lista_sup[0] # prendo per assoluto che il primo elemento sia il maggiore
        for elem in lista_sup  :
            if elem<massimo: #elemento fondamentale
                massimo=elem #scambio
        return massimo
    else:
        return None #se non è una lista ritorno None per far capire che c'è un problema


## Funzione myLen
#@input una lista 
#@return la lunghezza della lista
def myLen(lista):
    if isinstance( lista,list):
        contatore=0
        for e in lista  :
            contatore+=1
        return contatore
    else:
        return None

## Funzione myRange
#@input 2 numeri:
#   il primo numero inclusivo da cui parte la sequenza, se è con virgola viene troncato
#   il secondo numero escluso dove finisce la sequenza, se è con virgola viene troncato
#@return una lista con tutti i numeri interi che vanno dal primo numero al secondo numero
def myRange(nInclusive, nExclusive):
    nInclusive= int(nInclusive)
    nExclusive= int(nExclusive)
    lista=[]
   
    while(nInclusive<nExclusive):
        lista.append(nInclusive)
        nInclusive+=1
        
    return lista

##funzione di comodo
#viene creata una lista dinamica chiedendo dopo ogni inserimento se si vuole concludere oppure andare avanti nell'inserire elementi nella lista
#la funzione riesce a distinguere se gli elementi inseriti sono numeri o stringhe
def creaLista():
    lista=[]
    contatore=0
    while 1==1:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if elem.isnumeric():
            lista.append(int(elem))
        else :
            lista.append((elem))
        scelta=input("""\nVuoi inserire un nuovo elemento? \nNo -> 0\nSi -> qualsiasi altro tasto\n--> """)
        if scelta.find("0") != -1:
            return lista
        contatore+=1

print("""CIAO ~Simone Giacomini
Questo programma ha un menù dove puoi scegliere di usare delle funzioni riscritte da me come:
--len di una lista--    ->max di una lista<-    -<min di una lista>-    >>range di due valori<< 
""")




        

    

scelta=int(input(MENU))
while scelta != 0 :
    if scelta == 1 :
        print(CREALISTA)
        lista=creaLista()
        res=myLen(lista)
        if res !=None:
            print("La lista {} è lunga {}".format(lista, res))
        else: 
            print(PROBLEMA)
    elif scelta==2:
        print(CREALISTA)
        lista=creaLista()
        res=myMax(lista)
        if res !=None:
            print("L'elemento della lista {} più grande è {}".format(lista, res))
        else: 
            print(PROBLEMA)
    elif scelta==3:
        print(CREALISTA)
        lista=creaLista()
        res=myMin(lista)
        if res !=None:
            print("L'elemento della lista {} più grande è {}".format(lista, res))
        else: 
            print(PROBLEMA)
    elif scelta==4:
        n1=input("Inserisci il primo numero: ")
        n2=input("Inserisci il secondo numero: ")
        res=myRange(int(n1),int(n2))
        print("La lista creata è {}".format(res))
    else: 
        print(PROBLEMA+" il numero scelto non è valido")
    scelta=int(input(MENU))
print("Grazie di aver usato questo programma, buonagiornata =)")
