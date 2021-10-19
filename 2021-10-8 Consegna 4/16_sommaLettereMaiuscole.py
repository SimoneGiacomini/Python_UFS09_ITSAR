# Scrivere un programma Lunghezze che chiede all’utente di
# inserire una sequenza di stringhe e conclusa dalla stringa
# vuota, e poi stampa la somma delle lunghezze delle stringhe
# che iniziano con una lettera maiuscola. Per esempio, se si
# immettono le stringhe "Albero", "foglia", "Radici", "Ramo",
# "fiore" (e poi "" per finire), il programma stampa 16.

print("""CIAO ~Simone Giacomini
Questo programma chiede in input delle stringhe e se viene inserita un stringa vuota finisce,
alla fine calcola la somma delle lunghezza di solo le stringhe con i caratteri maiuscoli\n""")


stringa = "Simone"
somma = 0
while len(stringa)>0 :
    stringa = input("inserisci una parola, se inserisci una stringa vuota esci: ")
    if len(stringa)>0 :
        if stringa[0] >= "A" and stringa[0]<="Z" :
            somma+=len(stringa)
print ("la somma delle stringhe con la prima lettera maiuscola è "+str(somma))