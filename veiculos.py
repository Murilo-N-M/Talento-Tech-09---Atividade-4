from abc import ABC, abstractclassmethod

class Veiculos(ABC):
    def __init__(self, marca, modelo, ano, motor, cavalos):
        self.__marca = marca
        self.__ano = ano
        self.__motor = motor
        self.__cavalos = cavalos
        self.__modelo = modelo

    def getMarca(self):
        return self.__marca
    def getMotor(self):
        return self.__motor
    def getAno(self):
        return self.__ano
    def getCavalos(self):
        return self.__cavalos
    def getModelo(self):
        return self.__modelo
    
    def setMarca(self, marca):
        self.__marca = marca
    def setAno(self, ano):
        self.__ano = ano
    def setMotor(self, motor):
        self.__motor = motor
    def setCavalos(self, cavalos):
        self.__cavalos = cavalos
    def setModelo(self, modelo):
        self.__modelo = modelo

    @abstractclassmethod
    def mostrar(self):
        pass