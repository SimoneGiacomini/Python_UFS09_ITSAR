"""creare una lista: inserire manualmente un elenco di valori, terminando
con il valore 0"""

def creaLista():
    lista=[]
    contatore=0
    while 1==1:
        elem= input("Inserisci il {}° elemento della lista: ".format(contatore+1))      
        if elem!="0"  :
            lista.append(elem)
        else :
            return lista
        contatore+=1

print("La lista creata è {}".format(creaLista()))