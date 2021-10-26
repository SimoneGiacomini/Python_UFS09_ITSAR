"""creare una lista: inserire manualmente un elenco di valori, terminando
con il valore 0"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input delle stringhe qualsiasi, fino a quando non viene inserito "0"
"""

#questo metodo crea una lista, fino a quando non viene inserito "0"
def creaLista(elemento_conclusivo):
    lista=[]
    contatore=0
    while 1==1:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if elem != elemento_conclusivo:
            lista.append(elem)
        else :
            return lista
        contatore+=1


print(SALUTO)
print("La lista creata è {}".format(creaLista()))