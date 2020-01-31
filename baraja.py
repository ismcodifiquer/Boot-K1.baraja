import random

_palos = ['o', 'c', 'e', 'b']
_cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

def baraja():
    result = [] 
    for palo in _palos:
        for carta in _cartas:
            result.append(carta + palo)

    return result

def elige_carta(i, longitud):
    return random.randint(0, longitud-1)


def mezclar(b):
    for i in range(len(b)):
        # Elegimos carta de intercambio al azar
        al_azar = elige_carta(i, len(b))

        # Cambiamos carta por orden de (i) por la carta elegida al azar
        aux = b[i]
        b[i] = b[al_azar]
        b[al_azar] = aux
    return b

class Baraja():
    naipes = []
    __palos = ['o', 'c', 'e', 'b']
    __cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

    def __init__(self):
        self.naipes = []
        for palo in _palos:
            for carta in self.__cartas:
                self.naipes.append(carta + palo)

    def elige_carta(self, i):
        return random.randint(0, len(self.naipes)-1)
    
    def mezclar(self):
        for i in range(len(self.naipes)):
            # Elegimos carta de intercambio al azar
            al_azar = self.elige_carta(i)

            # Cambiamos la carta por orden (i) por la carta elegida al azar
            aux = self.naipes[i]
            self.naipes[i] = self.naipes[al_azar]
            self.naipes[al_azar] = aux

    def repartir(self, mano, jugadores):
        res = []
        for j in range(jugadores):
            res.append([])

        for c in range(mano):
            for item in res:
                carta = self.naipes.pop(0)
                item.append(carta)

        return res
