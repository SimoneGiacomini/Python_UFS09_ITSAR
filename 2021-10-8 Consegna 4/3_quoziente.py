#Dati due numeri scrivere il loro quoziente, se il divisore è diverso da 0 allora stampare la divisione altrimenti “impossibile” se il divisore = 0

print("""CIAO ~Simone Giacomini
Questo programma chiede in input due numeri e calcola il loro quoziente""")

dividendo = int(input("Inserisci il primo numero: "))
divisore = int(input("Inserisci il secondo numero NON INSERIRE 0: "))

# while divisore == 0 :
    # print("reinserisci il secondo numero, ricorda non mettere 0!")
    # divisore = int(input(-> ))

if divisore == 0 :
     print("il risultato è impossibile, in quanto hai inserito il divisore a 0")
    
else :
    risultato= dividendo/divisore 

    print("il quoziente è "+str(risultato))
    input("")