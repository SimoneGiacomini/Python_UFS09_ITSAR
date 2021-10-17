'''Riscrivete il programma ‘area.py’, definendo funzioni separate
per l’area del quadrato, del rettangolo e del cerchio (3.14 *
raggio**2). Il programma deve includere anche un’interfaccia a
menu
'''
MENU =  """MENU Principale\n1-> area quadrato\n2-> area rettangolo\n3-> area cerchio \n0-> finisci\n-> """

def areaRettangolo(lato1, lato2):
    return lato1*lato2
def areacerchio(raggio):
    return (raggio**2)*3.14



print("""CIAO ~Simone Giacomini
Questo programma permette di calcolare l'area del quadrato, del rettangolo oppure di un cerchio \n""")

scelta=int(input(MENU))
while scelta != 0 :
    if scelta ==1 :
        lato= int(input("inserisci il lato del quadrato: "))
        print("Il risultato dell'area di un quadrato con lato ({}) è uguale a ({})".format(lato, areaRettangolo(lato, lato)))
    elif scelta == 2:
        base= int(input("inserisci la base del rettangolo: "))
        altezza= int(input("inserisci l'area del rettangolo: "))
        print("Il risultato dell'area di un rettangolo con base=({}) ed altezza=({}) è uguale a {}".format(base,altezza,areaRettangolo(base,altezza)))
    elif scelta ==3:
        raggio=int(input("inserisci il raggio del cerchio: "))
        print("l'area di un cerchio con raggio=({}) è uguale a {}".format(raggio,areacerchio(raggio)))
    else:
        print("funzione inesistente! scegli bene! ")
    input("Premi un tasto per andare avanti-> ")
    scelta=int(input(MENU))

print("Grazie di aver usato questo programma, buonagiornata =)")
