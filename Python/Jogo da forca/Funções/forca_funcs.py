erro_0 = ("""
   |-------
   |      |
   |
   |
   |
   |
   |
___|___         """)

erro_1 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |
   |
   |
___|___         """)

erro_2 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |      |
   |      |
   |
___|___         """)

erro_3 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|
   |      |
   |
___|___         """)

erro_4 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |
___|___          """)

erro_5 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     /
___|___          """)

erro_6 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / \\
___|___          """)

def forca(vidas): # Função vidas foi criada para retornar o bonequinho do erro
    if vidas == 6:
        return erro_0
    elif vidas == 5:
        return erro_1
    elif vidas == 4:
        return erro_2
    elif vidas == 3:
        return erro_3
    elif vidas == 2:
        return erro_4
    elif vidas == 1:
        return erro_5
    else:
        return erro_6

def palavra(fruta,entradas):           #
  for letra in fruta:                  #
      if letra.lower() in entradas:    #
          print(letra, end=" ")        # Função para escrever a palavra escolhida no jogo
      else:                            #
          print("_", end=" ")          #
  print("")                            #


def separar():
  print('-'*50) # fiz essa funçao pra separar as rodadas no jogo

