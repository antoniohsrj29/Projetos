class Cliente:
    lista_cliente = []

    def __init__(self, cpf: str, nome: str, data_nascimento: str)-> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.desconto_idoso = verificar_idoso(datetime.strptime(data_nascimento, '%d/%m/%Y'))
        Cliente.lista_cliente.append(self)

    def __repr__(self) -> str:
        representacao = f"CPF: {self.cpf}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"
        return representacao

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 11:
            print("CPF não é valido.")
        else:
            self._cpf = cpf

    def buscar_cpf(cpf):
        cliente_buscado = None
        for cliente in Cliente.lista_cliente:
            if cpf == cliente.cpf:
                cliente_buscado = cliente
        return cliente_buscado