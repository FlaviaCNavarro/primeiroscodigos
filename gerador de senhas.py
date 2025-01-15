import random

letras= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Ola, vamos criar uma senha? ")
num = int(input("quantos numeros sua senha terá? "))
let = int(input("quantas letras sua senha terá? "))
sim = int(input("quantos simbolos expeciais? "))
x = num
senha = []

for a in range(1, num+1):
    escolha_numero =  random.choice(numeros)
    senha.append(escolha_numero)
for b in range(1,let+1):
    escolha_letra = random.choice(letras)
    senha.append(escolha_letra)
for c in range(1,sim+1):
    escolha_simbolos = random.choice(simbolos)
    senha.append(escolha_simbolos)

random.shuffle(senha)
senha = "".join(senha)
print(f"Sua senha é {senha}")
