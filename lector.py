class Conversor(object):
    def __init__(self):
        self.numeroOriginal = None
        self.baseNumeroOriginal = None
        self.numeroDecimal = None
        self.diccionario = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15,
            "g": 16,
            "h": 17,
            "i": 18,
            "j": 19,
            "k": 20,
            "l": 21,
            "m": 22,
            "n": 23,
            "ñ": 24,
            "o": 25,
            "p": 26,
            "q": 27,
            "r": 28,
            "s": 29,
            "t": 30,
            "u": 31,
            "v": 32,
            "w": 33,
            "x": 34,
            "y": 35,
            "z": 36
        }

        diccionario = {}
        for key in self.diccionario:
            diccionario[self.diccionario[key]] = key
        self.diccionario.update(diccionario)

        self.sumandosConvertidos = None

    def getNumero(self):
        self.numeroOriginal = input("dime el numero : ")
        self.baseNumeroOriginal = int(input("ahora dime en que base esta : "))
        self.numeroDecimal = self.converttoDec(self.numeroOriginal, self.baseNumeroOriginal)

    def converttoDec(self,numero, base):
        sumandos = list()
        sumandosConvertidos = list()
        numeroEnDecimal = 0
        potenciaPosition = 0

        for digito in numero:
            #print(digito)
            digitoConvertido = int(self.diccionario[digito])
            sumandos.append(digitoConvertido)
            #print(digitoConvertido)
        #print(sumandos)
        sumandos = sumandos[::-1]
        #print(sumandos)
        for digito in sumandos:
            valorDecimal = digito * (base**potenciaPosition)
            sumandosConvertidos.append(valorDecimal)
            numeroEnDecimal += valorDecimal
            potenciaPosition += 1

        print(sumandosConvertidos)
        print(numeroEnDecimal)
        self.sumandosConvertidos = sumandosConvertidos
        return numeroEnDecimal

    def ConvertToBase(self,baseDestino):
        numero = self.numeroDecimal
        pilaConversion = list()

        print("numero en decimal : " + str(numero))

        while numero > 0 :
            sigNumero = int(numero/baseDestino)
            nuevoDigito = numero%baseDestino
            if nuevoDigito is not 0 or base is 2:
                pilaConversion.append(nuevoDigito)
                print("nuevo valor : " + str(numero) + " | " + str(nuevoDigito))
            else:
                pilaConversion.append(sigNumero)
                print("nuevo valor : 0" + " | " + str(sigNumero))
            numero = sigNumero
        pilaConversion = pilaConversion[::-1]
        print(pilaConversion)


    def printNumber(self):
        print("numero : " + str(self.numeroOriginal))
        print("base   : " + str(self.baseNumeroOriginal))
        print("base 10: " + str(self.numeroDecimal))

Multiconversor = Conversor()

#print(Multiconversor.diccionario)

Multiconversor.getNumero()


while 1:
    opc = int(input("1- ver numero 2- recapturar numero 3- convertir numero\n -> "))
    if opc is 1:
        Multiconversor.printNumber()
    elif opc is 2:
        pass
    elif opc is 3:
        base = int(input("a que base quieres convertir el numero \n -> "))
        print("el numero " + str(Multiconversor.numeroDecimal))
        Multiconversor.ConvertToBase(base)