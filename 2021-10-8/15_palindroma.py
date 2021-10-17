"""Scrivere una funzione che dica se una parola è palindroma """


def isPalindroma(parola):
    lunghezza_parola=len(parola)
    contatore=1
    for i in parola:
        #se i è diverso dall'ultima lettera non controllata
        if i != parola[lunghezza_parola-contatore]:
            return False #sappiamo di sicuro che non sono uguali
        if contatore >( lunghezza_parola/2): #questo la valida, soprattutto per le parole palindrome dispari
            return True
        contatore+=1    
            
    

print("""CIAO ~Simone Giacomini
Questo programma permette di sapere se una parola è palindroma\n""")

parola= input("Inserisci una parola per sapere se è palindroma: ")
if isPalindroma(parola):
    print("La parola che hai inserito ({}) è palidroma".format(parola))
else:
    print("La parola che hai inserito ({}) NON è palidroma =(".format(parola))