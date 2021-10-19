#Dati due numeri, scrivere il maggiore (verificare anche se sono uguali

print("""CIAO ~Simone Giacomini
Questo programma chiede in input due numeri e dice qual è il MAGGIORE""")

numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

if numero1==numero2:
     print("i numeri sono uguali ("+str(numero1)+")")

elif numero1>numero2 :
    print("il primo numero ("+str(numero1)+") è maggiore")
else :
    print("il secondo numero ("+str(numero2)+") è maggiore")