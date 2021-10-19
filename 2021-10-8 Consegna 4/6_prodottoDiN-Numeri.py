#Dati n numeri scrivere il loro prodotto

print("""CIAO ~Simone Giacomini
Questo programma chiede in input quanti numeri vuoi memorizzare e scrive il loro Prodotto""")
quanti = int(input("Quanti numeri vuoi moltiplicare?\n->"))
i=0
prodotto=1
while(i<quanti):
    n= int(input("Inserisci il "+str(i+1)+"° numero: "))
    if n==0 :
        prodotto*= n 
        break
    prodotto*= n 
    i+=1
if n>0 :
    print("il prodotto è uguale a "+str(prodotto))
else :
    print("il prodotto è già stato calcolato, in quanto hai inserito 0 \nIl prodotto è 0")