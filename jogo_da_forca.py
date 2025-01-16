import random

palavras = ["capivara","vaca","jumento","cerveja","abacaxi", "zoológico", "quimbamba", "girassol", "zeitgeist", "quixotesco", "ziguezague", "onírico", "efêmero", "saudade"]

sorteio = random.choice(palavras)
b = len(sorteio)
print(f"Não olhe viu!{sorteio}")
print("_"*b)
adivinha = input("Chute uma letra: ").lower()

forca  = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |[
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
vidas = 6
chutes = []
repetidas = []
fim = False
while fim == False:
    display = ""
    if adivinha in repetidas:
        print("Essa letra ja foi")
        adivinha = input("Tente mais uma letra ")
    else:
            for a in sorteio:
                if a == adivinha:
                    display += a
                    chutes.append(adivinha)
                    repetidas.append(adivinha)
                elif a in chutes:
                    display += a
                else:
                    display += "_"
            if vidas > 0:
                if adivinha in sorteio:
                     print(forca[vidas])
                     print(f"+++++++++voce ainda tem {vidas} vidas!++++++++++")
                else:
                     vidas -= 1
                     print(forca[vidas])
                     print("essa letra não tem na palavra")
                     print(f"+++++++se foi uma vida. Agora voce tem {vidas} vidas*********")

                if display == sorteio:
                    fim = True
                    print("voce acertou")

                print(display)
                adivinha = input("mais uma letra: ")
            else:
                print('voce perdeu')
                print(sorteio)
                fim = True