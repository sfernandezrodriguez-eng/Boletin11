import pickle
import os
from Tarefa import Tarefa


class Xestor_Tarefas:
    def __init__(self):
        self.archivo = 'ficheiro.pkl'
        self.listaTarefas = []
        # Cargamos los datos solo una vez al principio
        self.cargar_datos()

    def cargar_datos(self):
        """Carga inicial de datos con manejo de errores si el archivo no existe."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'rb') as fich:
                    self.listaTarefas = pickle.load(fich)
            except (EOFError, pickle.UnpicklingError):
                self.listaTarefas = []
        else:
            self.listaTarefas = []

    def gardar_datos(self):
        """Método único para volcar toda la lista al archivo pkl."""
        try:
            with open(self.archivo, 'wb') as fich:
                pickle.dump(self.listaTarefas, fich)
            print("\n[SISTEMA] Datos sincronizados en el archivo correctamente.")
        except Exception as e:
            print(f"Error crítico al guardar: {e}")

    def engadir_tarefa(self):
        try:
            data = int(input("Día (número): "))
            hora = int(input("Hora (número): "))
        except ValueError:
            print("Error: El día y la hora deben ser números.")
            return

        duracion = input("Duración: ")
        nome = input("Nombre: ")
        descricion = input("Descripción: ")
        estado = input("Estado: ")

        nueva_tarefa = Tarefa(data, hora, duracion, nome, descricion, estado)
        self.listaTarefas.append(nueva_tarefa)
        print(f"Tarea '{nome}' añadida a la sesión actual.")

    def modificar_tarefa(self):
        nome_a_cambiar = input("Nombre de la tarea a modificar: ")
        for tarea in self.listaTarefas:
            if tarea.nome == nome_a_cambiar:
                print(f"Modificando: {tarea.nome}")
                opcion = input("¿Qué quieres cambiar? (nome, data, hora, descricion): ").lower()
                if opcion == "nome":
                    tarea.nome = input("Nuevo nombre: ")
                elif opcion == "data":
                    tarea.data = input("Nueva data: ")
                elif opcion == "hora":
                    tarea.hora = input("Nueva hora: ")
                elif opcion == "descricion":
                    tarea.descricion = input("Nueva descripción: ")
                print("Cambio realizado en memoria.")
                return
        print("No se encontró la tarea.")

    def borrar_tarefa_por_nome(self):
        nome_a_borrar = input("Nombre de la tarea a borrar: ")
        original_len = len(self.listaTarefas)
        self.listaTarefas = [t for t in self.listaTarefas if t.nome != nome_a_borrar]

        if len(self.listaTarefas) < original_len:
            print(f"Tarea '{nome_a_borrar}' eliminada de la sesión.")
        else:
            print("No se encontró la tarea.")

    def menu(self):
        opcion = -1
        while opcion != 0:
            print("\n--- Xestion de Tarefas (Sesión Activa) ---")
            print("1. Agregar tarea")
            print("2. Borrar tarea")
            print("3. Modificar tarea")
            print("4. Ver listado actual")
            print("0. Gardar e Saír")  # El guardado ocurre aquí

            try:
                opcion = int(input("Elige una opción: "))
            except ValueError:
                continue

            if opcion == 1:
                self.engadir_tarefa()
            elif opcion == 2:
                self.borrar_tarefa_por_nome()
            elif opcion == 3:
                self.modificar_tarefa()
            elif opcion == 4:
                if not self.listaTarefas:
                    print("La lista está vacía.")
                else:
                    for i, t in enumerate(self.listaTarefas):
                        print(f"{i + 1}. {t.nome} | Día: {t.data} | Estado: {t.estado}")
            elif opcion == 0:
                self.gardar_datos()  # ÚNICA LLAMADA AL DISCO
                print("Cerrando programa...")


if __name__ == "__main__":
    xestor = Xestor_Tarefas()
    xestor.menu()