#2021-10-14
#Dato un numero scrivere se è multiplo di 10

print("""CIAO ~Simone Giacomini
Questo programma chiede in input un numero e controlla se è multiplo di 10""")

n= int(input("Inserisci il numero da controllare: "))
if n%10==0 :
    print(str(n)+" è multiplo di 10")
else :
    print(str(n)+" NON è multiplo di 10")
input("")
