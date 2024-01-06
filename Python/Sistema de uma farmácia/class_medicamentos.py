from class_laboratorio import Laboratorio
class Medicamento:
    lista_de_medicamentos = []
    id_med = 1
    def __init__(self, nome: str, composto: str, laboratorio:Laboratorio, descricao: str, preco: float)-> None:
        self.nome = nome
        self.composto = composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.preco = preco
        self.id_med = Medicamento.id_med
        Medicamento.id_med += 1
        Medicamento.lista_de_medicamentos.append(self)

    def __repr__(self):
        representacao = f"ID: {self.id_med} - Nome: {self.nome} - Preço: {self.preco}"
        return representacao


    def buscar_medicamento(id_med):
        if id_med == 0:
           return 0
        else:
          medicamento_buscado = None
          for medicamento in Medicamento.lista_de_medicamentos:
              if id_med == medicamento.id_med:
                  medicamento_buscado = medicamento
          return medicamento_buscado

class MedicamentoFitoterapico(Medicamento):
    lista_de_fitos = []
    def __init__(self, nome: str, composto: str, laboratorio:Laboratorio, descricao: str, preco: float)-> None:
        super().__init__(nome,composto,laboratorio,descricao,preco)
        MedicamentoFitoterapico.lista_de_fitos.append(self)

class MedicamentoQuimioterapico(Medicamento):
    lista_de_quimios = []
    def __init__(self, nome: str, composto: str, laboratorio: Laboratorio, descricao: str, necessita_receita: str, preco : float)-> None:
        super().__init__(nome, composto, laboratorio, descricao,preco)
        self.necessita_receita = necessita_receita
        MedicamentoQuimioterapico.lista_de_quimios.append(self)