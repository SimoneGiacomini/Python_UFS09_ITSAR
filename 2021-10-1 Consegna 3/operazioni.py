#Scrivete un programma che mostra l’utilizzo delle 4 operazioni matematiche

print ("Questo programma mostra l'utilizzo delle 4 operaizioni")


numero2= 0
numero1 = int (input ("Inserisci il primo numero: "))
while numero2 == 0:
    numero2 = int (input ("Inserisci il secondo numero(non inserire lo 0): "))


print ("La somma è: " + str (numero1+numero2))
print ("La moltiplicazione è: " + str (numero1*numero2))
if numero2 != 0:
    print ("La divisione è: " + str (numero1/numero2))
else :
    print("LA DIVISIONE TRA {} e {} è impossibile!".format(numero1, numero2))
print ("La sottrazione è: " + str (numero1-numero2))

input (" ")
   
