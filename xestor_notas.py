class Xestor_Notas:
    def __init__(self, ruta):
        self.__ruta = ruta

    def engadir_nota(self, texto):
        if isinstance(texto, str):
            with open(self.__ruta,'a') as notas:
                notas.write(f"{texto}\n")

    def leer_notas(self):
        with open(self.__ruta, 'r') as notas:
            print(notas.read())


    def buscar_clave(self, palabra):
        with open(self.__ruta, 'r') as notas:
            lineas = notas.readlines()
            for linea in lineas:
                if palabra in linea:
                    print(linea)



if __name__ == "__main__":
    xestor = Xestor_Notas('notas.txt')
    # xestor.engadir_nota('Lore ipsum')
    # xestor.leer_notas()
    xestor.buscar_clave('Tercera')