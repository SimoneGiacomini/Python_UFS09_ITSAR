"""Scrivere una classe Lampadina che mi consenta di modellare il suo stato
“acceso/spento”, mi consenta di compiere delle azioni “accendi e spegni” e
sapere il suo stato attuale. Chiedere all’utente di inserire un valore intero N e di
creare N lampadine"""

from typing import Tuple


SALUTO = """CIAO ~Simone Giacomini
Questo programma permette di creare una lista di oggetti lampadina e di gestirle
"""


class Lampadina:
    #attributi :
    #identificatore -> str. DEFAULT = ""
    #stato -> bool. DEFAULT = False. False indica spento


    # Costruttore
    def __init__(self, ident="", stato=False):
        self.__identificatore = ident
        self.__stato = stato

    # OUTPUT A VIDEO
    def __str__(self) -> str:
        output = "ID: "+self.__identificatore+"; STATO:"+self.getStatoStr+";"
        return output

    # get per attributo __identificatore
    def getIdentificatore(self) -> str:
        return self.__identificatore

    def getStato(self) -> bool:
        return self.__stato

    def getStatoStr(self) -> str:
        if(self.__stato):
            return "accesa"
        else:
            return "spenta"

    def cambiaStato(self) -> bool:
        self.__stato = not self.__stato
        return self.__stato


def traduciAccesaSpenta(inp) -> bool:
    inp = str(inp).lower()
    l_false = [" 0 ", " spento ", " off ", " false ", " spenta ", " falso ", " non accesa ", " non acceso "]
    for el in l_false:
        if inp is el:
            return False
    return True


def creaListaLampadine(numero_di_lampadine):
    lista = []
    contatore=0
    for i in range(0, numero_di_lampadine):
        id_lampadina = input("\nInserisci il nome della {} lampadina: ".format(contatore+1))
        stato_lampadina = traduciAccesaSpenta(
            input("\nLa vuoi accesa o spenta la lampadina {}?: ".format(id_lampadina)))
        lista.append(Lampadina(id_lampadina, stato_lampadina))
        contatore+=1
    return lista


# MAIN
print(SALUTO)
numero_lampadine = input("inserisci quante lampadine vuoi creare: ")
while not numero_lampadine.isnumeric():
    print("Non hai inserito un numero, riprova")
    numero_lampadine = input("inserisci quante lampadine vuoi creare: ")
my_lista = creaListaLampadine(int(numero_lampadine))




""" 
---------------@Deprecated---------------------------
class Lampadario: # boh non ci ho capito niente
    
    __listaLampadine=[] #una lista di lampadine
    __lampadinePresenti=len(__listaLampadine)

    def __init__(self, lista_lampadine=[]) -> bool:
        if not isinstance(lista_lampadine,list()): #se l'argomento passato non è una lista 
            return False # ALLORA RITORNA FALSO
        else: #altrimenti 
            for lamp in lista_lampadine:
                if not isinstance (lamp,Lampadina()): # oppure se uno degli elementi passati non è una lampadina
                    return False  # ALLORA RITORNA FALSO
            self.__listaLampadine=lista_lampadine # se invece va tutto bene copio la lista passata 
            return True #e ritorno vero 

    def addLampadina(self, lampadina_to_add) -> bool:
        if isinstance(lampadina_to_add, Lampadina()):
            self.__listaLampadine.append(lampadina_to_add)
            return True
        else:
            return False
    
    def cambiaStatoLampadina(self,nome_lampadina) ->bool :
        for el in self.__listaLampadine:
            if el.getIdentificatore() is nome_lampadina:
                

                return True
        return False

    def addLampadine(self,lista_lampadine=[]) -> bool:
        pass #funzione che per completezza si dovrebbe aggiungere

    def delLampadina(self, nome_lampadina) -> bool:
        pass #funzione che per completezza si dovrebbe aggiungere

     """
