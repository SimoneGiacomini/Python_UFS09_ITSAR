#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma permette di creare una lista di numeri e restituisce la mediana
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
        scelta=input("""\nVuoi inserire un nuovo elemento? \nSi -> qualsiasi altro tasto\nNo -> 0\n--> """)
        if scelta.find("0") == 0:
            return lista
        contatore+=1

#funzione richiesta
def mediana(lista):
    lunghezza_lista = len(lista)
    if lunghezza_lista == 0:
        return None
    lista= sorted(lista)
    if lunghezza_lista%2 == 0:
        lunghezza_lista= lunghezza_lista//2
        return (lista[lunghezza_lista]+lista[lunghezza_lista-1])/2
    else:
        return lista[(lunghezza_lista//2)]

#inizio programma
lista=creaLista()
risultato = mediana(lista)
if risultato is None :
    print("La lista è vuota")
else:
    print("La mediana della lista {} è uguale a {}".format(lista,risultato))

