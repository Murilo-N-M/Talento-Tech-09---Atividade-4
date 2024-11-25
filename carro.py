from veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, marca, modelo, ano, motor, cavalos, nPortas):
        super().__init__(marca, modelo, ano, motor, cavalos)
        self.__nPortas = nPortas

    def getNPortas(self):
        return self.__nPortas
    
    def setNPortas(self, nPortas):
        self.__nPortas = nPortas

    def mostrar(self):
        return (f"Carro da marca: {self.getMarca()}, do modelo: {self.getModelo()}, do ano: {self.getAno()}, com o motor: {self.getMotor()} de {self.getCavalos()} cavalos e com {self.getNPortas()} portas")
    
# c = Carro("Vw", "Gol", 2005, "VM 2", 57, 4)
# print (c.mostrar())