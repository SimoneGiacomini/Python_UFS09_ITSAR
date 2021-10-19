#Data la base e l’altezza di un triangolo, scrivere l’area. Successivamente richiedere le tre
#lunghezze dei lati per stampare il perimetro calcolato

print ("Questo programma mostra l'area di un triangolo e chiede 3 lati per il perimetro in centimetri")

base = int (input ("Inserisci Base: "))
altezza = int (input ("Inserisci altezza: "))

area = (base*altezza)/2
print ("\nL'area è: " + str(area))

cateto1 = int (input ("\nInserisci il primo cateto: "))

cateto2 = int (input ("Inserisci il secondo cateto: "))

cateto3 = int (input ("Inserisci il terzo cateto: "))


perimetro = cateto3+cateto1+cateto2
print ("\nIl perimetro è " + str(perimetro))

input(" ")
