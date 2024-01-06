class Laboratorio:
    lista_de_laboratorios = []
    def __init__(self, nome: str, endereco: str, telefone:int, cidade: str, estado: str)-> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        Laboratorio.lista_de_laboratorios.append(self)

    def __repr__(self):
        representacao = f"Laboratorio {self.nome}, tel: {self.telefone}"
        return representacao

    def buscar_laboratorio(nome_laboratorio):
        laboratorio_buscado = None
        for lab in Laboratorio.lista_de_laboratorios:
          if nome_laboratorio == lab.nome:
            laboratorio_buscado = lab
        return laboratorio_buscado