"""Scrivere una funzione che dica se un numero è primo o no"""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma chiede in input un numero e scopre se è primo o no"
"""

##questa funzione ritorna vero se il numero passato è primo,
#falso altrimenti
def isPrimo(numero):
    if numero==2:
        return True
    if numero%2==0:
        return False

    div=0 #quanti dividendi ha?
    
    for e in range(1,numero+1): #controllo tutti i numeri da 1 al numero stesso (numero+1 è necessario in quanto l'ultimo numero è esclusivo) 
        if (numero%e) ==0: #e è un divisore di numero? 
            div+=1  
    
    if(div>2):
        return False
    else :
        return True


##Funzione che utilizza le eccezioni trovata su stack overflow, fa un check se il parametro passato è effetiva un numero
def isNumber(numero):
    try:
        int(numero)
        return True
    except:
        return False


print(SALUTO)
numero_primo= input("Inserisci ora il numero da controllare: ")
while not isNumber(numero_primo):
    numero_primo= input("Il valore che hai inserito non è un numero intero\nriprova: ")
numero_primo=int(numero_primo)    
if isPrimo(numero_primo):
    print("{} è un numero primo!".format(numero_primo))
else:
     print("{} NON è un numero primo =( ".format(numero_primo))