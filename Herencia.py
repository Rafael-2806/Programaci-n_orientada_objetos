
class Pokemon:
    
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def __str__(self):
        return"{} es un pokemon de tipo:{}".format(self.nombre,self.tipo)
    
class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque {}".format(self.nombre,tipo_ataque)

class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque {}".format(self.nombre,tipo_ataque)
    
nuevo_pokemon= Pokemon("boby", "electrico")
print(nuevo_pokemon.__str__())
    
new_pokemon= Pikachu("boby", "electrico")
print(new_pokemon.ataque("impaacto trueno"))
    
        