# class enfermedad pre-def
class Peste_negra():
    def __init__(self):
        self.infect_probabilidad = 0.0012
        self.dias_sanar = 2
        self.enfermo = None
        self.contador = None

    def get_infect_probabilidad(self):
        return self.infect_probabilidad
    
    def set_infect_probabilidad(self, infect_probabilidad):
        self.infect_probabilidad = infect_probabilidad

    def get_dias_sanar(self):
        return self.dias_sanar
    
    def set_dias_sanar(self, dias_sanar):
        self.dias_sanar = dias_sanar

    def get_enfermo(self):
        return self.enfermo
    
    def set_enfermo(self, enfermo):
        self.enfermo = enfermo

    def get_contador(self):
        return self.contador
    
    def set_contador(self, contador):
        self.contador = contador

    