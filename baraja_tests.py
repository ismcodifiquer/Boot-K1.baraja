import unittest
from unittest.mock import patch
import baraja

def mi_elige_carta(i, longitud):
    if i == longitud-1:
        return 0
    else:
        return i+1

class BarajaTest(unittest.TestCase):

    def test_crear_baraja(self):
        b = baraja.baraja()
        self.assertEqual(len(b), 40) 
    
        self.assertEqual(b[0], 'Ao')
        self.assertEqual(b[39], 'Rb')
        self.assertEqual(b[10], 'Ac')
        self.assertEqual(b[20], 'Ae')

    @patch('baraja.elige_carta', mi_elige_carta)
    def test_mezclar_lista(self):
        b = ['A', 'B', 'C', 'D', 'E']
        mezclada = ['A', 'C', 'D', 'E', 'B']
        b = baraja.mezclar(b)
        self.assertEqual(b, mezclada)

    
if __name__ == '__main__':
    unittest.main()
