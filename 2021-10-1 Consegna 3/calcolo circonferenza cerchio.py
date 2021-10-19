#Scrivere un programma che svolga l’area e perimetro di un cerchio chiedendo da input il
#raggio, visualizzando i risultati ottenuti


pigreco= 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
print ("Questo programma calcola l'area e la circonferenza di un cerchio dato il raggio")

raggio = int (input ("Inserisci il raggio: "))

print ("La circonferenza è di " + str(raggio*pigreco*2))

area = (raggio*raggio)*pigreco
print ("L'area è di " + str(area))
input("")

