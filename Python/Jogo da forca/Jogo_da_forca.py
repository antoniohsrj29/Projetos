from Funções.forca_funcs import * 
from random import randrange
with open ('C:/Users/Pichau/Desktop/Portifolio/Projetos/Python/Jogo da forca/frutas.txt','r') as arquivo_frutas: # Com with não há a preocupação em escrever a linha de "close" arquivo
  conteudo = arquivo_frutas.read()
lista_palavras = conteudo.split()  # Divide o conteúdo do arquivo em palavras

def Jogo_da_forca():
  game_on = True
  while game_on:
    jogar = input("Você gostaria de jogar o jogo da forca? S ou N ")
    if jogar.lower() in ['sim','yes', 's', 'y']:
            acertos = 0
            entradas = []
            entradas_erradas = []
            palpites_errados = []
            vidas = 6
            fruta_escolhida = lista_palavras[randrange(len(lista_palavras))]
            separar()
            print("Bem-vindo ao jogo da forca!")
            print(f"A fruta tem {len(fruta_escolhida)} letras:")
            while vidas != 0 and acertos != len(fruta_escolhida):
                print(forca(vidas),end = '    ')
                palavra(fruta_escolhida,entradas)
                if entradas_erradas != []:
                    print(f"Letras erradas: {entradas_erradas}")
                if palpites_errados != []:
                    print(f"Palavras erradas: {palpites_errados}")
                print(f"Você tem {vidas} vidas.")
                # lê tentativa válida
                tentativa = input("Agora é sua vez, escolha uma letra: ")
                while tentativa.lower() in entradas:
                    print("Você ja digitou essa opção.")
                    tentativa = input("Escolha novamente: ")
                entradas.append(tentativa.lower())
                separar()
                # valida letra
                if len(tentativa) == 1 :
                    if tentativa in fruta_escolhida:
                        print('Você acertou a letra.')
                        acertos = acertos + fruta_escolhida.count(tentativa)
                    else:
                        entradas_erradas.append(tentativa)
                        vidas = vidas -1
                        print(f"Voce errou a letra, por isso perdeu uma vida.")
                # valida palpite
                else:
                    if tentativa == fruta_escolhida:
                        acertos = len(fruta_escolhida)
                        print('Você acertou a palavra.')
                    else:
                         palpites_errados.append(tentativa)
                         vidas = vidas -1
                         print(f"Você errou a palavra, por isso perdeu uma vida.")
            if vidas == 0:
                separar()
                print(f"Você perdeu, a palavra era {fruta_escolhida}")
            else:
                separar()
                print(f"Parabens você venceu, a fruta era {fruta_escolhida}")
    elif jogar.lower() in ["n",'nao','não']:
        print("Uma pena não querer jogar.")
        game_on = False
    else:
        print("Resposta invalida.")
