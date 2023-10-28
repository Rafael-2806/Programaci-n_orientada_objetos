

class Persona:
    
    def __init__(self,nombre, año):
        self.nombre = nombre
        self.año = año
    def __str__(self):
        return "{} tiene {} años".format(self.nombre, self.año)
    def comentario(self,frase):
        return "{} dice: {}".format(self.nombre,frase)
    
doctor=Persona('Mario',25)

print(doctor.comentario('comemela'))
    
