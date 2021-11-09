class Empresa:
    def __init__(self):
        pass

class Empleados(Empresa):
    def __init__(self):
        pass
    #def __init__(self,DirGen, Gerente, RecHumanos ): 
    #    self.DirGen = DirGen
    #    self.Gerente = Gerente
    #    self.RecHumanos = RecHumanos
        
class Persona:
    def __init__(self, Persona):
        self.Persona = Persona

class Vestimenta: 
    def __init__(self):
        pass
    
    def Vestir(self):
        print(type(self).__name__,"Que buen Estilo")
        
    
class VesFormal(Vestimenta):
    def __init__(self, saco, pantVestir, camisa, corbata, zapatos):
        self.saco = saco
        self.pantVestir = pantVestir
        self.camisa = camisa
        self.corbata = corbata
        self.zapatos = zapatos
        
    def Vestir(self):
        print("El Usuario porta un Traje muy elegante")
        
class VesInfromal(Vestimenta):
    def __init__(self, playera, pantMezclilla, tennis):
        self.playera = playera
        self.pantMezclilla = pantMezclilla
        self.tennis = tennis
        
    def Vestir(self):
        print("El Usuario posee Vestimenta Informal")
        
        
        