"""Creare un programma che chieda all’utente di inserire una stringa di lunghezza pari.
Se l’utente inserisce una stringa dispari, il programma dovrà chiedergli di reinserirla
fino a che non inserisca una stringa di lunghezza pari."""

#costanti
SALUTO ="""CIAO ~Simone Giacomini
Questo programma continua a chiedere in input una stringa finchè non se ne aggiunge una di lunghezza pari"
"""
#funzioneisStringaPari
def isStringaPari(stringa):
    if len(stringa)%2==0:
        return True
    else:
        return False


print(SALUTO)
stringa = input("Inserisci dunque la stringa: ")
while not isStringaPari(stringa):
    stringa=input("La stringa \n\"{}\"\nnon è di lunghezza pari,\nreinseriscila: ".format(stringa))
print("La stringa {} è di lunghezza pari".format(stringa))