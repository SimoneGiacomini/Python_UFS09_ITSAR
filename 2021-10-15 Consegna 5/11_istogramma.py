"""Scrivere una funzione che produce un istogramma esempio Istrogramma([4,2,6]):"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input una lista di numeri e poi li converte in istogrammi"
"""

#crea una stringa con tanti caratteri quanti quelli indicati in lunghezza
def disegnaRiga(lunghezza, carattere):
    str=""
    for i in range(0,lunghezza):
        if i!=0 and i % 10 ==0:
            str+="'"
        str+=carattere
    return str

#Data una lista stampa tanti caratteri quanti quelli indicati per ogni elemento della lista
def disegnaIstogramma(lista, carattere="O"):
    quanti_spazi=len(str(max(lista))) #trovo l'elemento maggiore in modo da indentare al meglio l'istogramma
    for elem in lista:
        spazio=""
        cifre_elem=len(str(elem))
        if cifre_elem< quanti_spazi:
            for s in range(cifre_elem,quanti_spazi):
                spazio+=" "    
        stringa_disegnata=disegnaRiga(elem,carattere)
        print("{}({}){}".format(spazio,elem,stringa_disegnata))
        
##funzione che crea una lista
#viene creata una lista dinamica chiedendo dopo ogni inserimento se si vuole concludere oppure andare avanti nell'inserire elementi nella lista
#la funzione riesce a distinguere se gli elementi inseriti sono numeri o stringhe
def creaLista():
    lista=[]
    contatore=0
    while 1==1:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if elem.isnumeric()  :
            num=int(elem)
            """if num<0 :
                print("NON Puoi inserire un numero negativo")
                contatore-=1
            else:"""
            lista.append(num)
        else :
            print("\nL'Input inserito non è un numero")
            contatore-=1 #si sottrae in quanto non è un input soddisfacente, ciclo sfalsato
        scelta=input("""\nVuoi inserire un nuovo elemento? \nNo -> 0\nSi -> qualsiasi altro tasto\n--> """)
        if scelta.find("0") == 0:
            return lista
        contatore+=1

#inizio programma
print(SALUTO)
print("creiamo dunque la lista:\n")
lista=creaLista()
print(max(lista))
print("L'istogramma della lista {} è:\n".format(lista))
disegnaIstogramma(lista,"#")