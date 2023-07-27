from enfermedad import Peste_negra
import json
import random

with open('nombres_apellidos.json') as file:
    data = json.load(file)

# class persona pre-def
class Persona(Peste_negra):
    def __init__(self):
        self._id = 0
        self.nombre = str
        self.id_apellido = str
        self.enfermo = False # contraer enfermedad
        self.vivo = True #True = vivo, False = muerto
        self.recuperado = False 

    #funcion para crear personas
    def crear_persona(self,can_per) :
        cont = 0
        personas = []
        while cont != can_per:
            self._id = self._id + 1
            nom = random.choice(data["nombres"])
            ape = random.choice(data["apellidos"])
            persona =[self._id,nom,ape,self.enfermo,self.vivo,self.recuperado]
            personas.append(persona)
            cont = cont + 1
        p = random.choice(personas)
        personas.remove(p)
        p[3]= True
        personas.append(p)
        return personas

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id_apellido(self):
        return self.id_apellido
    
    def set_id_apellido(self, id_apellido):
        self.apellido = id_apellido

    def get_tener_enfermedad(self):
        return self.tener_enfermedad
    
    def set_tener_enfermedad(self, tener_enfermedad):
        self.tener_enfermedad = tener_enfermedad

    def get_life(self):
        return self.life
    
    def set_life(self, life):
        self.life = life