#Scrivere un programma che svolga l’area e perimetro di un rettangolo chiedendo da
#input la base e altezza, visualizzando i risultati ottenuti

print ("Questo programma calcola l'area e il perimetro di un rettangolo tramite base e altezza")


base = int (input("Inserisci base: "))
altezza = int (input("Inserisci l'altezza: "))
perimetro = (base + altezza)*2
area = base*altezza

print ("\nL'area è " + str(area) + " e il perimetro è " + str(perimetro))



