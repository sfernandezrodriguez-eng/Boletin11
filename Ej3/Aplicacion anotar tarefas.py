import pickle
from Tarefa import Tarefa
class Xestor_Tarefas:
    def __init__(self):
        self.listaTarefas = []
        self.leer_datos_binario('ficheiro.pkl')

    def engadir_tarefa(self):
        try:
            data = int(input("Que dia es: "))
            hora = int(input("Que hora es: "))
        except ValueError:
            print("Error: El día y la hora deben ser números.")
            return
        duración = input("Cuanto vas a durar: ")
        nome = input("Nombre de la tarea: ")
        descrición = input("Descripción de la tarea: ")
        estado = input("Estado de la tarea: ")
        nueva_tarefa = Tarefa(data, hora, duración, nome, descrición,estado)
        self.listaTarefas.append(nueva_tarefa)
        try:
            with open('ficheiro.pkl', 'wb') as fich:
                pickle.dump(self.listaTarefas, fich)
            print("Tarea guardada correctamente.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def modificar_tarefa(self):
        nome_a_cambiar = input("Introduce o nome da tarefa que queres modificar: ")
        encontrada = False

        for tarefa in self.listaTarefas:
            if tarefa.nome == nome_a_cambiar:
                encontrada = True
                print(f"Modificando: {tarefa.nome}")
                print("¿Que quieres cambiar? (nome, data, hora, duracion, descricion, estado)")
                opcion = input("Opción: ").lower()
                if opcion == "nome":
                    tarefa.nome = input("Novo nome: ")
                elif opcion == "data":
                    tarefa.data = input("Nova data: ")
                elif opcion == "hora":
                    tarefa.hora = input("Nova hora: ")
                elif opcion == "descricion":
                    tarefa.descricion = input("Nova descrición: ")
                print("Tarefa modificada con éxito.")
                with open('ficheiro.pkl', 'wb') as fich:
                    pickle.dump(self.listaTarefas, fich)
                break

        if not encontrada:
            print("Non se atopou a tarefa.")

    def borrar_tarefa_por_nome(self):
            nome_a_borrar = input("Introduce o nome da tarefa que queres borrar: ")
            encontrada = False
            for tarefa in self.listaTarefas:
                if tarefa.nome == nome_a_borrar:
                    self.listaTarefas.remove(tarefa)
                    encontrada = True
                    print(f"Tarefa '{nome_a_borrar}' borrada con éxito.")
                    break

            if not encontrada:
                print("Non se atopou ningunha tarefa con ese nome.")
            else:
                with open('ficheiro.pkl', 'wb') as fich:
                    pickle.dump(self.listaTarefas, fich)


    def leer_datos_binario(self, ficheiro):
        with open(ficheiro, 'rb') as fich:
            self.listaTarefas = pickle.load(fich)

    def menu(self):
        opcion = 999
        while opcion != 0:
            print("\n--- Xestion del almacén ---")
            print("1. Agregar unha nova tarefa")
            print("2. Borrar unha tarefa")
            print("3. Modificar unha tarefa")
            print("4. Leer o listado de tarefas.")
            print("0. Salir")
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                self.engadir_tarefa()
            elif opcion == 2:
                self.borrar_tarefa_por_nome()
                print("Se ha guardado correctamente")
            elif opcion == 3:
                self.modificar_tarefa()
                print("Se ha guardado correctamente")
            elif opcion == 4:
                self.leer_datos_binario('ficheiro.pkl')
                if not self.listaTarefas:
                    print("Non hay tareas gardadas.")
                else:
                    for i, tarea in enumerate(self.listaTarefas):
                        print(f"{i + 1}. {tarea.nome} Día: {tarea.data} Hora: {tarea.hora} Duracion: {tarea.duración}   Descricion: {tarea.descrición}  Estado: {tarea.estado} ")
                print("--------------------------\n")
            elif opcion == 0:
                print("Saliendo del programa...")
            else:
                print("Opción no válida.")




if __name__ == "__main__":
    xestor = Xestor_Tarefas()
    xestor.menu()