import Tipo

class TipoFuego():

    def __init__(self, tipo ='Fuego', soy_fuerte_frente = 'Tierra', soy_debil_frente = 'Aire'):
        self.tipo = tipo
        self.soy_fuerte_frente = soy_fuerte_frente
        self.soy_debil_frente = soy_debil_frente

    def __str__(self):
        return " %s: %s, %s" %(self.tipo, self.soy_fuerte_frente, self.soy_debil_frente)