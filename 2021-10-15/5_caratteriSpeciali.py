"""Creare un programma che chieda all’utente di inserire un numero n e stampi
una stringa lunga n caratteri dove i caratteri che la compongono saranno i
caratteri @ e # alternati partendo con un carattere @
Ad esempio se l’utente dice che la stringa dovrà essere lunga 5 caratteri la
stringa stampata dovrà essere: @#@#@"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input una lunghezza, e stampa in modo concatenato "@" e "#" in sequenza"
"""

def stampaSpeciale(cifra, carattere1="@", carattere2="#"):
    stringa=""
    for e in range(0,cifra):
        if e%2==0 :
            stringa+=carattere1
        else:
            stringa+=carattere2
    return stringa

print (SALUTO)
lunghezza="hola"
while not lunghezza.isdecimal():
    lunghezza = input("Inserisci la lunghezza della stringa speciale da creare\n-> ")
    
    if not lunghezza.isdecimal():
        print("\n>>>>VALORE INSERITO NON è UN NUMERO INTERO<<<<<\n")

lunghezza=int(lunghezza)
print("La stringa speciale creata è {}".format(stampaSpeciale(lunghezza)))
