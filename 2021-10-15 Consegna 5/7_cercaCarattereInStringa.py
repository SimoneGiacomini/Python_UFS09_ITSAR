#consegna
"""Creare una funzione che abbia due parametri: una stringa e un carattere. La
funzione dovrà scorrere tutte le lettere della stringa utilizzando l'istruzione for
e restituire il numero di occorrenze del carattere nella stringa."""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input una stringa ed un carattere e controlla quante volte quel carattere è presente nella stringa"
"""

#si potrebbe più semplicemente usare la funzione embedded count, ma visto la consegna ho deciso di farla come segnato
def myCountInString(stringa, carattere):
    #stringa=stringa.lower()
    #carattere= carattere.lower()
    contatore=0
    for c in stringa:
        if c==carattere:
            contatore+=1
    return contatore

#inzio programma
print(SALUTO)
stringa=input("Inserisci dunque una stringa qualsiasi: ")
carattere=input("Inserisci un solo carattere: ")
while len(carattere)>1:
    carattere=input("\nATTENZIONE hai inserito una stringa!\nInserisci un solo carattere: ")
print("\nIl numero di volte che il carattere '{}' compare in '{}' è di {} volte ".format(carattere,stringa,myCountInString(stringa,carattere)))