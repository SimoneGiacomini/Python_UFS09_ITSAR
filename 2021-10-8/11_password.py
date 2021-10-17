#Scrivete un programma che chieda all’utente di indovinare una
#password, ma che dia al giocatore solamente 3 possibilità, fallite le quali
#il programma terminerà, stampando “È troppo complicato per voi”

print("""CIAO ~Simone Giacomini
Questo programma chiede di indovinare la una password. Buona Fortuna!""")

password = "passworddifficile"
contatore = 3
sgamata="no"
while contatore > 0 :
    sgamata = input("prova ad indovinare la password, tentativi rimasti %d: " %contatore)
    contatore -=1
    if(sgamata == password) :
        print ("Hai trovato la password giusta")
        contatore=-1
    else :
        print("password errata\n")
if contatore== 0 :
    print("È troppo complicato per voi")