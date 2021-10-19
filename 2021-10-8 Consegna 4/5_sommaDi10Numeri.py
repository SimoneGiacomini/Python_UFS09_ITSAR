#Dati 10 numeri scrivere la loro somma, numeri inseriti ad ogni iterazione

print("""CIAO ~Simone Giacomini
Questo programma chiede in input 10 numeri e scrive la loro somma""")
i=0
somma = 0
while(i<10):
    n= int(input("Inserisci il "+str(i+1)+"° numero: "))
    somma+= n 
    i+=1
print("la somma è uguale a "+str(somma))
