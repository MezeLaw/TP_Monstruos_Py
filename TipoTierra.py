import Tipo

class TipoTierra():

    def __init__(self, tipo = 'Tierra', soy_fuerte_frente = 'Aire', soy_debil_frente = 'Agua'):
        self.tipo = tipo
        self.soy_fuerte_frente = soy_fuerte_frente
        self.soy_debil_frente = soy_debil_frente

    def __str__(self):
        return " %s: %s, %s" %(self.tipo, self.soy_fuerte_frente, self.soy_debil_frente)