"""Scrivere una funzione che produca una lista dei numeri di Fibonacci fino ad n (senza far uso delle
liste, ma usando un ciclo su una lista e documentarsi sul metodo append)"""


#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma produce una lista di numeri di Fibonacci fino ad il numero inserito
"""
def fibonacci(n):
    f0=0
    f1=1
    lista=[f0]
    if n==0:
         lista.append(f0)
         return lista
    elif n<0:
        return None 
    else:
        lista.append(f1)

    while f0+f1<=n:
        n_calcolato=f0+f1
        f0=f1
        f1=n_calcolato
        lista.append(n_calcolato)

    return lista
    

print(SALUTO)
numero_inserito = input("Inserisci ora il numero: ")
while (not numero_inserito.isnumeric()): #finchè "numero_inserito "non è un numero e è minore di 0 
    numero_inserito = input(
        "Il valore che hai inserito non è un numero naturale\nriprova: ")
numero_inserito = int(numero_inserito)
print("La serie di Fibonacci fino a {} è {}".format(numero_inserito,fibonacci(numero_inserito)))
