
#                   ************** PROGRAMACION AVANZADA **************

#                        ///// MODELAR GERENTE \\\\\
#Enunciado: Escriba una aplicacion que modele en el paradigma orientado a objetos el siguiente escenario.
   
#        El gerente de la empresa es un empleado que mide 1.8 m, se llama <nombre> y tiene puesto un saco
#        con tres botones. En este momento el gerente esta entrevistando a una persona para su contratacion.

#        ALUMNA: Sarahi Romano Guerra        

      
    
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.edad = edad

class Empresa:
    def __init__(self,nombreEmp,numEmpl):
        self.__nombreEmp = nombreEmp
        self.numEmpl = numEmpl
        
class Empleados(  Empresa):
    def __init__(self,  nombre, apellido, edad, carrera,cel):
        self.__nombre =nombre
        self.__Apellido = apellido
        self.edad = edad
        self.__numCel = cel
        self.carrera = carrera
        
        
class Gerente(Empleados):
    def __init__(self, salario,nombre, apellido, edad, carrera, cel):
        self.salario = salario
        super().__init__(self, nombre, apellido, edad, carrera, cel)
        
class SolicitarEmpleo(Persona):
    def __init__(self, nombre, apellido, edad, Especialidad):
        self.Especialidad = Especialidad
        super().__init__(nombre, apellido, edad)
        

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
        
        
        