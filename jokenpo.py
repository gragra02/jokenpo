# Jokenpo em Python
import random
from time import sleep

print ("=-" * 20)
print ("Escolha um item para jogar Jokepo =>" )
esperar = sleep(1)
print ("[0} Pedra, [1] Papel, [2] Tesoura")
jogador = int(input("Qual é a sua jogada? "))

print ("JO")
esperar = sleep(1)
print ("KEN")
esperar = sleep(1)
print ("PO!!!") 
esperar = sleep(1)
itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0, 2)
print (f"Computador jogou {itens[computador]} ")
if jogador == 0:
    if computador == 0:
        print ("Empate!")
    elif computador == 1:
        print ("Computador Venceu!")
    elif computador == 2:
        print ("Jogador VEnceu! ")
elif jogador == 1:
    if computador == 0:
        print ("Jodado Venceu!")
    elif computador == 1:
        print ("Empate!")
    elif computador == 2:
        print ("Computador Venceu!")
    elif jogador == 2 :
        if computador  == 0:
            print ("Computador Venceu!")
        elif computador == 1:
            print ("Jogador Venceu!")
        elif computador == 2:
            print ("Empate!")
        else:
            print ("Jogada inválida! Tente novamente.")


