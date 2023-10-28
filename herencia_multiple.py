
class Telefono:
    pass
    def __init__(self):
        pass
    
    def llamar(self):
        print("llamando...")
    
    def ocupado(self):
        print("ocupado...")
    
class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("tomado fotos...")
        
class Reproduccion:
    def __init__(self):
        pass
    def reproducionmusica(self):
        print("reproduciendo musica")
    def reproduccionvideo(self):
        print("reproduciendo video")
    

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self): #limpiar recurso del
        print("telefono apagado")
    

movil =smartphone()
print(movil.fotografia())
print(movil.llamar())