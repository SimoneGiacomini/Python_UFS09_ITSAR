#Questo programma chiede in input un numero e dice se è positivo o negativo

print("""CIAO ~Simone Giacomini
Questo programma chiede in input un numero e dice se è positivo o negativo""")
numero = int(input("Inserisci un numero: "))
if numero == 0 :
    print("il numero è 0")
elif numero > 0 :
     print("il numero è positivo")
else :
    print("il numero è negativo")
    
input("")
