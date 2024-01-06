def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):
    return a / b

def multiplicacao(a,b):
    return a * b

def exponencial(a,b):
    return a ** b

def calcule():
    try:
        a = float(input('Digite o primeiro numero: '))
    except:
        print(f"Digite um numero por favor.")
        resultado = "Não foi possivel fazer operação"
        return resultado
    try:
        b = float(input('Digite o segundo numero: '))
    except:
        print(f"Digite um numero por favor.")
        resultado = "Não foi possivel fazer operação"
        return resultado
    operacao = input("""Escolha uma das operações abaixo:
                     + para soma;
                     - para subtração;
                     / para divisão;
                     * para multiplicação;
                     ** para elevar um numero ao outro:
                     """)
    if operacao not in ['+','-','/','*','**']:
        print("Operação não identificada!")
        resultado = "Não foi possivel realizar a operação."
    elif operacao == '+':
        print(f"a soma é {soma(a,b)}")
        resultado = soma(a,b)
    
    elif operacao == '-':
        print(f"a subtração é {subtracao(a,b)}")
        resultado = subtracao(a,b)
    
    elif operacao == '/':
        print(f"a divisão é {divisao(a,b)}")
        resultado = divisao(a,b)
    
    elif operacao == '*':
        print(f"a multiplicação é {multiplicacao(a,b)}")
        resultado = multiplicacao(a,b)
    
    elif operacao == '**':
        print(f"a exponecial é {exponencial(a,b)}")
        resultado = exponencial(a,b)
    
    return resultado
