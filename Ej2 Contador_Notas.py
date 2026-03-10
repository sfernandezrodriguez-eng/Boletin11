class Contador_Notas:
    def __init__(self, ruta):
        self.__ruta = ruta
        self.cont = 0


    def contar_palabras(self,palabra):
        with open(self.__ruta, 'r') as notas:
            lineas = notas.readlines()
            for linea in lineas:
                palabras_en_linea = linea.split()
                for word in palabras_en_linea:
                        if word==palabra:
                            self.cont += 1
            print(self.cont)

if __name__ == "__main__":
    xestor = Contador_Notas('notas.txt')
    xestor.contar_palabras('linea')