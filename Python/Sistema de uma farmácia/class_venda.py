from datetime import datetime
from class_cliente import Cliente

class Venda:
    vendas_realizadas = {}
    ganhos_totais = 0
    clientes_atendidos = []
    quantidade_do_medicamento = {}
    remedios_vendidos = []
    def __init__(self, data_hora: datetime, cliente: Cliente)-> None:
        self.data_hora = data_hora
        self.cliente = cliente
        if self.cliente.nome not in Venda.clientes_atendidos:
            Venda.clientes_atendidos.append(self.cliente.nome)


    def remedio_mais_vendido():
        count_mais_vendido = 0
        nome_mais_vendido = 0
        for medic in Venda.quantidade_do_medicamento:
          if Venda.quantidade_do_medicamento[medic] > count_mais_vendido:
              count_mais_vendido = Venda.quantidade_do_medicamento[medic]
              nome_mais_vendido = medic
          else:
              pass
        return nome_mais_vendido

    def somar_ao_ganhos_totais(valor):
        Venda.ganhos_totais += valor