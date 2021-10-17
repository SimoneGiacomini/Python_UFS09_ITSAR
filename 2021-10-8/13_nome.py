''' Scrivete un programma che chieda all’utente il nome. Se viene inserito il
vostro nome, il programma dovrà rispondere con un “Questo è un bel
nome”, se il nome inserito è Mario Rossi o Giuseppe Verdi il programma
dovrà rispondere con una battuta ;) mentre in tutti gli altri casi l’output
del programma sarà un semplice “Tu hai un bel nome!”'''




def cercaNome(nomeInserito, nomeDaConfrontare) :
    nomeInserito= nomeInserito.lower()
    nomeDaConfrontare=   nomeDaConfrontare.lower()
    if nomeInserito in nomeDaConfrontare:
        return True
    else :
        return False

mioNome="Simone Giacomini"
marioRossi= "Mario Rossi"
giuseppeVerdi= "Giuseppe Verdi"

print("""CIAO ~Simone Giacomini
Questo programma chiede in input un nome, poi accadono cose magiche rispetto a quello che inserisci\n""")
nome= input("inserisci un nome ")

if cercaNome(nome, mioNome):
    print("Questo è un bel nome")
elif cercaNome(nome, marioRossi): 
    print ("IT'S A ME MARIO")
elif cercaNome(nome, giuseppeVerdi): 
    print ("Nabucco best rap track")
else :
    print("Tu hai un bel nome")