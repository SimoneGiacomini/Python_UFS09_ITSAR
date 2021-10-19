#Inserire n numeri diversi da 0 (0 per finire), contare quanti sono i numeri inseriti
print("""CIAO ~Simone Giacomini
Questo programma chiede in input n numeri, se inserisci 0 finisce.\nConta quanti sono i numeri inseriti diversi da 0\n""")
i=0
n=1
while n!= 0 :
	n= int(input("Inserisci un numero, se inserisci 0, esci: "))
	i+=1
#tolgo uno in quanto ho contato in più per l'ultimo numero inserito
i-=1 
print("Hai inserito "+str(i)+" numeri")

