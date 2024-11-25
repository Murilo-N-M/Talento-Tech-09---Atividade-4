from veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, marca, modelo, ano, motor, cavalos):
        super().__init__(marca, modelo, ano, motor, cavalos)

    def mostrar(self):
        return (f"A moto da marca {self.getMarca()}, do modelo: {self.getModelo()}, do ano: {self.getAno()} e com o motor: {self.getMotor()} de {self.getCavalos()} cavalos")
    
# m = Moto("Nissan", "Vespa", 1978, "V4", 32)
# print (m.mostrar())