### Descrição do Trabalho

Implementar uma aplicação para uma Farmácia que vende produtos através de e-commerce.

O trabalho deve ser feito individual ou em grupos(definido pelo professor e/ou conjunto com a turma).

### Funcionlidades

A farmácia precisa dos seguintes serviços (que devem ser disponibilizados para escolha do usuário através de um menu feito no console. Não é necessário implementar interface gráfica):

Deverá conter um cadastro de clientes, no qual a busca se dará por CPF (sem pontuação)

Deverá conter um cadastro de medicamentos, no qual a busca se dará pelo nome, fabricante ou descrição parcial de acordo com o tipo de medicamento. Os medicamentos poderão ser Quimioterápicos ou Fitoterápicos. Os medicamentos Quimioterápicos deverão ter a informação sobre se são vendidos apenas mediante receita ou não (Ex: remédios tarja preta e antibióticos).

Através do sistema deverá ser possível efetuar vendas, e estas serão realizadas apenas para clientes cadastrados no sistema.

Durante a venda, haverá 20% de desconto para clientes idosos (acima de 65 anos), e 10% de desconto nas compras acima de 150 reais. Os descontos não são cumulativos, e deve ser dado sempre o desconto mais alto caso haja conflito.

Durante a venda de remédios Quimioterápicos, se um dos remédios for do tipo controlado (que exige apresentação de receita para a compra), o sistema deverá emitir um alerta ao atendente questionando se o mesmo verificou a receita do respectivo remédio. Deverá ser informado no alerta o nome do remédio controlado.

Deverá ser possível emitir relatórios:

De listagem de clientes, cadastrados por nome, em ordem alfabética crescrente (A-Z), especificando os dados do cliente
De listagem de medicamentos, por ordem alfabética
De listagem de medicamentos Quimioterápicos ou Fitoterápicos
Estatísticas dos atendimentos realizados no dia (considere o dia como o tempo que o menu está em execução. Quando for sair do programa, deve ser emitido este relatório) contendo:
Remédio mais vendido, contendo a quantidade e o valor total
Quantidade de pessoas atendidas
Número de remédios Quimioterápicos vendidos no dia, contendo a quantidade e o valor
Número de remédios Fitoterápicos vendidos no dia, contendo a quantidade e o valor