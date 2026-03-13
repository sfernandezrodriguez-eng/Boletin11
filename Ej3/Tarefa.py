class Tarefa:
    def __init__(self, data, hora, duración, nome, descrición,  estado):
        self.data = data
        self.hora = hora
        self.duración = duración
        self.nome = nome
        self.descrición = descrición
        self.estado = self.setEstado(estado)



    def setEstado(self,estado):
        if estado=='feita' or estado=='non feita':
            self.estado=estado
        else:
            return ValueError


    def __str__(self):
        return self.nome, self.data, self.hora,self.duración,self.descrición,self.estado