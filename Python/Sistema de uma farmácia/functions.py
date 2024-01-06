from class_cliente import Cliente
from class_laboratorio import Laboratorio
from class_medicamentos import Medicamento
from class_medicamentos import MedicamentoFitoterapico
from class_medicamentos import MedicamentoQuimioterapico
from class_venda import Venda
from datetime import datetime

def verificar_idoso(data: datetime):
    IDADE_IDOSO = 65
    if (datetime.today().year - data.year - ((datetime.today().month, datetime.today().day) < (data.month, data.day))) >= IDADE_IDOSO:
      return True
    else:
      return False

def cadastrar_cliente():
    cpf = input("CPF do cliente: ")
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento do cliente: ")
    Cliente(cpf, nome, data_nascimento)
    print("Cliente cadastrado com sucesso.")

def cadastrar_medicamento(Laboratorio):
    nome = input("Nome do medicamento: ")
    composto = input("Principal composto do medicamento: ")
    laboratorio = Laboratorio
    descricao = input("Descrição do medicamento: ")
    preco = float(input("Preço do medicamento: "))
    opcao = input('Digite Q para QUIMIOTERÁOICO  e F para FITOTERÁPICO: ').lower()
    if opcao == 'q':
      necessita_receita = input("Necessita de receita? (S/N): ").lower()
      MedicamentoQuimioterapico(nome, composto, laboratorio, descricao, necessita_receita,preco)
      print("Medicamento quimioterápico cadastrado com sucesso.")
    elif opcao == 'f':
      MedicamentoFitoterapico(nome, composto, laboratorio, descricao,preco)
      print("Medicamento fitoterápico cadastrado com sucesso.")

def cadastrar_laboratorio():
    nome = input("Nome do laboratório: ")
    endereco = input("Endereço do laboratório: ")
    telefone = input("Telefone do laboratório: ")
    cidade = input("Cidade do laboratório: ")
    estado = input("Estado do laboratório: ")
    laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
    print("Laboratório cadastrado com sucesso.")
    return laboratorio

def efetuar_venda():
    compra = []
    fmt = "{:15}|{:^15}|R$ {:<10.2f}"
    comprador = Cliente.buscar_cpf(input("CPF do cliente: "))
    preco_final = 0
    if comprador is None:
        print("Cliente não encontrado.")
        return
    else:
        while True:
            print("\nListagem de Medicamentos:")
            for medicamento in Medicamento.lista_de_medicamentos:
                print(medicamento)
            produto = Medicamento.buscar_medicamento(int(input("Digite o ID do medicamento(Digite '0' para encerrar as vendas): ")))

            if produto == 0:
                break
            elif produto != None:
                quantidade = input('entre com a quantidade - ')
                compra.append((produto.nome,int(quantidade),int(quantidade)*produto.preco,f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}"))
                if produto.nome in Venda.quantidade_do_medicamento:
                    Venda.quantidade_do_medicamento[produto.nome] += int(quantidade)
                else:
                    Venda.quantidade_do_medicamento[produto.nome] = int(quantidade)
                    Venda.remedios_vendidos.append(produto)
                preco_final += int(quantidade)*produto.preco
            else:
                print("Produto não encontrado.")

    if comprador.cpf in Venda.vendas_realizadas:
        Venda.vendas_realizadas[comprador.cpf].append(compra)
    else:
        Venda.vendas_realizadas[comprador.cpf] = compra

    print('Cliente: {:<45}'.format(comprador.cpf))
    print('-------------------------------------------')
    print('{:15}|{:^15}|R$ {:<10}'.format('Produtos','Quantidade','Valor'))
    print('-------------------------------------------')
    for i, j, k, l_ in compra:
        print(fmt.format(i,j,k))
    print('-------------------------------------------')
    print('{:<31}|R$ {:<.2f}'.format('Sub_TOTAL',preco_final))
    print('-------------------------------------------')
    if comprador.desconto_idoso == True:
        preco_final = preco_final * 0.8
        print(f'Com desconto, o valor da venda foi para {preco_final:.2f}!')
    elif preco_final > 150:
        preco_final = preco_final * 0.9
        print(f'Com desconto, o valor da venda foi para {preco_final:.2f}!')
    else:
        print(f"O valor da venda {preco_final:.2f}")
    Venda(datetime.today(),comprador)
    Venda.somar_ao_ganhos_totais(preco_final)


def emitir_relatorios():
    # Listagem de clientes em ordem alfabética
    print("\nListagem de Clientes:")
    for cliente in sorted(Cliente.lista_cliente, key=lambda x: x.nome):
        print(cliente)

    # Listagem de medicamentos em ordem alfabética
    print("\nListagem de Medicamentos:")
    for medicamento in sorted(Medicamento.lista_de_medicamentos, key=lambda x: x.nome):
        print(f"Nome: {medicamento.nome}, Composto: {medicamento.composto}, Laboratório: {medicamento.laboratorio.nome}")

    # Listagem de medicamentos quimioterápicos
    print("\nListagem de Medicamentos Quimioterápicos:")
    for medicamento in MedicamentoQuimioterapico.lista_de_quimios:
        necessita_receita = "Sim" if medicamento.necessita_receita else "Não"
        print(f"Nome: {medicamento.nome}, Laboratório: {medicamento.laboratorio.nome}, Necessita Receita: {necessita_receita}")

    print("\nListagem de Medicamentos Fitoterápicos:")
    for medicamento in MedicamentoFitoterapico.lista_de_fitos:
        print(f"Nome: {medicamento.nome}, Laboratório: {medicamento.laboratorio.nome}")

    # Estatísticas dos atendimentos
    total_pessoas_atendidas = len(Venda.clientes_atendidos)
    total_vendas = len(Venda.vendas_realizadas)
    med_mais_vendido = Venda.remedio_mais_vendido()
    total_qt_quimioterapicos = sum(1 for venda in Venda.remedios_vendidos if isinstance(venda, MedicamentoQuimioterapico))
    total_valor_quimioterapicos = sum(float(remedio.preco*Venda.quantidade_do_medicamento[remedio.nome]) for remedio in Venda.remedios_vendidos if isinstance(remedio, MedicamentoQuimioterapico))
    total_qt_fitoterapicos = sum(1 for venda in Venda.remedios_vendidos if isinstance(venda, MedicamentoFitoterapico))
    total_valor_fitoterapicos = sum(float(remedio.preco*Venda.quantidade_do_medicamento[remedio.nome]) for remedio in Venda.remedios_vendidos if isinstance(remedio, MedicamentoFitoterapico))

    print("\nEstatísticas dos Atendimentos:")
    print(f"Total de pessoas atendidas: {total_pessoas_atendidas}")
    print(f"Total de vendas realizadas: {total_vendas}")
    print(f'Remédio mais vendido do dia: {med_mais_vendido}')
    print(f"Total de medicamentos quimioterápicos vendidos: {total_qt_quimioterapicos} (Valor Total: R${total_valor_quimioterapicos:.2f})")
    print(f"Total de medicamentos fitoterápicos vendidos: {total_qt_fitoterapicos} (Valor Total: R${total_valor_fitoterapicos:.2f})")
