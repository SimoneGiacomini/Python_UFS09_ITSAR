#Data la base e l’altezza di un triangolo, scrivere l’area.

print ("Questo programma calcola l'area di un triangolo")

base = int (input ("Inserisci Base: "))
print ("Hai inserito " + str ( base))
altezza = int (input ("Inserisci altezza: "))
print ("Hai inserito " + str(altezza))
if base == 0 or altezza == 0 :
    print("l'area è 0")
else :
    area = (base*altezza)/2
    print ("\nL'area è: " + str(area))