""""
Scrivere una classe Bottiglia che mi consenta di modellare il suo stato (quantità
e contenuto, esempio: acqua, cocacola, Fanta). Tale classe mi consente di
compiere delle azioni “bevi” o “riempi” su una bottiglia e sapere il suo stato
attuale (quantità e contenuto). Chiedere all’utente di inserire un valore intero da
input che indica su quale bottiglia del Distributore effettuare l’operazione
desiderata, stampandone le azioni effettuate. Il Distributore mette a disposizione
5 bottiglie (le prime 3 di acqua, la quarta di CocaCola e la quinta di Fanta)

"""

class Bottiglia:
    #ATTRIBUTI:
    #quantità -> intero
    #contenuto -> stringa
    def __init__(self, capacita, contenuto):
        self.capacita=capacita
        self.setQuantita (capacita)#va a riprendere la funzione del set
        self.contenuto=contenuto
    
    def setQuantita(self, quantita):
        if quantita<0:
            self.quantita=0
        else:
            self.quantita=quantita

    def getCapacitaBottiglia(self):
        return self.capacita

    def getQuantita(self):
        return self.quantita
    def getContenuto (self):
        return self.contenuto
    def bevi(self,quantita_bevuta_dame):
        self.quantita -= quantita_bevuta_dame
    def riempi(self, quantita_aggiunta):
        self.quantita += quantita_aggiunta
    def __str__(self):
        return str(self.contenuto) + " " + str(self.quantita)
""""
Chiedere all’utente di inserire un valore intero da
input che indica su quale bottiglia del Distributore effettuare l’operazione
desiderata, stampandone le azioni effettuate. Il Distributore mette a disposizione
5 bottiglie (le prime 3 di acqua, la quarta di CocaCola e la quinta di Fanta)
"""
class Distributore:
    #ATTRIBUTI
    #lista da 5 elementi di tipo bottiglia

    def __init__(self,tupla):
        self.tupla=tupla #la tupla che mi arriva dall'esterno me la salvo al mio interno e diventa la mia
    
    def __str__(self):
        contatore=1
        stringa_fin=""
        for i in self.tupla:
            stringa_fin=stringa_fin + "bottiglia "+ str(contatore)+" "+ i.__str__() + "\n"
            contatore+=1
        return stringa_fin
    
    def getTupla(self):
        return self.tupla

#questo metodo ritorna la bottiglia scelta in base alla poisizione di input inserita
    def scelta_bottiglia(self, n): #n mi indica la posizione all'interno del mio distributore
        return self.tupla[n]
    
    def bevi_da_una_bottiglia(self, n, quantita_da_bere):
        self.tupla[n].bevi(quantita_da_bere)
    
    def riempi_bottiglia(self, n, quantita_da_riempire):
        self.tupla[n].riempi(quantita_da_riempire)


#questo funzione crea un distributore con all'interno 5 bottiglie (le prime 3 di acqua, la quarta di CocaCola e la quinta di Fanta)
def crea_distributore():
    miatupla=(Bottiglia(1000, "acqua"),Bottiglia(1000, "acqua"), Bottiglia(1000, "acqua"), Bottiglia(750, "cocacola"), Bottiglia(800, "fanta"))
    distributore=Distributore(miatupla)
    return distributore

def traduciRiempiBevi(inp) -> bool:
    inp = str(inp).lower()
    l_false = " riempi riempire fill refill "
    if inp in l_false:
        return False
    elif inp == "non bere":
        return False
    return True



#main
mio_distributore=crea_distributore()




stato=True

while stato:
    print (mio_distributore)
    n=int(input("scegli dunque che bottiglia vuoi usare: "))

    while n <1 or n>5:
        n=int(input("Numero inserito inesistente\nscegli dunque che bottiglia vuoi usare: "))

    n-=1
    my_s=mio_distributore.scelta_bottiglia(n).__str__()
    inp=input("Vuoi bere o riempire la bottiglia? '{}' ".format(my_s))

    if traduciRiempiBevi(inp):
        mio_distributore.bevi_da_una_bottiglia(n,150)
    else:
        mio_distributore.riempi_bottiglia(n,150)

    inp=input("vuoi continuare ad utilizzare il distributore?\n(SI/NO)")
    if(inp in "NO"):
        stato=False

