from functions import *

while True:
    print("\nMenu:")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Medicamento")
    print("3. Cadastrar Laboratório")
    print("4. Efetuar Venda")
    print("5. Emitir Relatórios")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        laboratorio = Laboratorio.buscar_laboratorio(input('De qual laboratorio é o medicamento? '))
        if laboratorio != None:
            pass
        else:
            print('Laboratorio ainda não cadastrado, por favor cadastre-o')
            laboratorio = cadastrar_laboratorio()
        cadastrar_medicamento(laboratorio)
    elif opcao == '3':
        cadastrar_laboratorio()
    elif opcao == '4':
        efetuar_venda()
    elif opcao == '5':
        emitir_relatorios()
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")