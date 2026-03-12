class Contador_Notas:
    def __init__(self, ruta,conteo):
        self.__ruta = ruta
        self.conteo = conteo
        self.cont = 0
        self.lista=[]

    def contar_todas_las_palabras(self):
        frecuencias = {}

        with open(self.__ruta, 'r') as notas:
            for linea in notas:
                palabras = linea.split()
                for palabra in palabras:

                    palabra = palabra.lower().strip(",.")

                    if palabra in frecuencias:
                        frecuencias[palabra] += 1
                    else:
                        frecuencias[palabra] = 1
        for palabra, contar in frecuencias.items():
            print(f"La palabra '{palabra}' aparece {contar} veces.")
            hola = (f"La palabra '{palabra}' aparece {contar} veces.")
            with open(self.conteo,'a') as cont:
                cont.write(f"{hola}\n")


if __name__ == "__main__":
    xestor = Contador_Notas('notas.txt','conteo.txt')
    xestor.contar_todas_las_palabras()