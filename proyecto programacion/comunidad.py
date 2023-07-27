from enfermedad import Peste_negra

#class comunidad pre-def
class Comunidad(Peste_negra):
    def __init__(self):
        self.cantidad_persona = None
        self.prom_contacto = 0   
        self.enfermedad = Peste_negra()
        self.num_infectado = 0
        self.posibilidad_de_infect = None 


    def get_cantidad_persona(self):
        return self.cantidad_persona
    
    def set_cantidad_persona(self, cantidad_persona):
        self.cantidad_persona = cantidad_persona

    def get_prom_contacto(self):
        return self.prom_contacto
    
    def set_prom_contacto(self, prom_contacto):
        self.prom_contacto = prom_contacto

    def get_enfermedad(self):
        return self.enfermedad
    
    def set_enfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def get_num_infectado(self):
        return self.num_infectado
    
    def set_num_infectado(self, num_infectado):
        self.num_infectado = num_infectado

    def get_posibilidad_de_infect(self):
        return self.posibilidad_de_infect
    
    def set_posibilidad_de_infect(self, posibilidad_de_infect):
        self.posibilidad_de_infect = posibilidad_de_infect