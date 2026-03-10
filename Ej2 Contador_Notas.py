class Contador_Notas:
    def __init__(self, ruta):
        self.__ruta = ruta
        self.cont = 0

    def engadir_nota(self, texto):
        if isinstance(texto, str):
            with open(self.__ruta,'a') as notas:
                notas.write(f"{texto}\n")

    def leer_notas(self):
        with open(self.__ruta, 'r') as notas:
            print(notas.read())

    def contar_palabras(self,palabra):
        with open(self.__ruta, 'r') as notas:
            lineas = notas.readlines()
            for linea in lineas:
                    if palabra in linea:
                            self.cont += 1
            print(self.cont)

if __name__ == "__main__":
    xestor = Contador_Notas('notas.txt')
    xestor.contar_palabras('linea')