#Dati 10 numeri scrivere la loro somma, numeri inseriti ad ogni iterazione

print("""CIAO ~Simone Giacomini
Questo programma chiede in input 10 caratteri ed un altro carattere C\ninseguito controlla se C è uno dei caratteri inseriti precedentemente\n""")
i=1
stringa= input("Inserisci il "+str(i)+"° carattere: ")
while(i<10):
    n= (input("Inserisci il "+str(i+1)+"° carattere: "))
    stringa+= n 
    i+=1

print("i caratteri inseriti sono "+str(stringa))
n= (input("Inserisci il  carattere da confrontare: "))
if n in stringa :
    print (n+" è all'interno di "+stringa)
else:
     print (n+" NON è all'interno di "+stringa)
input("")
