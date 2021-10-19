''' Scrivete un programma che chieda due numeri. Se la somma dei due
numeri supera 100, stampate “Numero troppo grande” '''

print("""CIAO ~Simone Giacomini
Questo programma chiede in input 2 numeri.
Se la somma dei due numeri supera 100, verrà stampato “Numero troppo grande” \n""")

i=0
somma=0
while(i<2):
    n= int(input("Inserisci il "+str(i+1)+"° numero: "))
    somma+=n
    i+=1

if somma > 100 :
    print("Numero troppo grande")
else :
    print("La sommma è uguale a {}".format(somma))