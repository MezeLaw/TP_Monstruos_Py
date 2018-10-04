class Tipo(object):

    def __init__(self, tipo, soy_fuerte_frente, soy_debil_frente):
        ##"Constructor de Tipo"
        self.tipo = tipo
        self.soy_fuerte_frente = soy_fuerte_frente
        self.soy_debil_frente = soy_debil_frente

    def __str__(self):
        return " %s: %s, %s" %(str(self.tipo), self.soy_fuerte_frente, self.soy_debil_frente)
