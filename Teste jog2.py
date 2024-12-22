import ipywidgets as widgets
from IPython.display import display
import random
import time

button = widgets.Button(description="Clique-me")
def on_button_click(b):
    print("Botão clicado!")

text_input = widgets.Text(
    placeholder='Digite algo aqui'  # Texto que aparece antes de começar a digitar
)
display(text_input)


button.on_click(on_button_click)

display(button)


class Personagem:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.ouro = 0
        self.xp = 0


    def atacar(self, criatura):
        dano_caused = random.randint(0, self.dano)
        criatura.vida -= dano_caused
        print(f"{self.nome} atacou a criatura e causou {dano_caused} de dano!")

    def curar(self, quantidade):
        self.vida += quantidade
        print(f"{self.nome} recuperou {quantidade} de vida!")

    def ganhar_ouro(self, quantidade):
        self.ouro += quantidade
        print(f"{self.nome} ganhou {quantidade} de ouro!")

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")

    def escolher_peculiaridade(self):
        print("\nEscolha o que melhorar:")
        print("1. Aumentar Vida (+10)")
        print("2. Aumentar Dano (+5)")
        escolha = input("Digite 1 ou 2: ")
        if escolha == '1':
            self.curar(10)
        elif escolha == '2':
            self.dano += 5
        else:
            print("Escolha inválida, você não ganhou melhorias!")

#Monstro
class Criatura:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self, personagem):
        dano_caused = random.randint(0, self.dano)
        personagem.receber_ataque(dano_caused)
        print(f"A criatura atacou e causou {dano_caused} de dano!")

    def batalha(personagem, criatura):
      while personagem.vida > 0 and criatura.vida > 0:
        # O jogador ataca
        personagem.atacar(criatura)
        time.sleep(1)  # Pausa para dar mais ritmo ao jogo

        # A criatura ataca de volta
        if criatura.vida > 0:
            criatura.atacar(personagem)
            time.sleep(1)  # Pausa para dar mais ritmo ao jogo

        # Mostra o status após cada turno
        print(f"Vida do {personagem.nome}: {personagem.vida}")
        print(f"Vida da Criatura: {criatura.vida}")
        print("-" * 20)

        # Checando se alguém morreu
        if personagem.vida <= 0:
            print(f"{personagem.nome} foi derrotado!")
            return False  # Jogador perdeu
        elif criatura.vida <= 0:
            print(f"{personagem.nome} derrotou a criatura!")
            personagem.ganhar_ouro(random.randint(5, 20))
            personagem.ganhar_xp(random.randint(10, 50))
            return True  # Jogador venceu

def main():
    nome = input("Digite o nome do seu personagem: ")
    personagem = Personagem(nome, vida=100, dano=15)
    print(f"\nBem-vindo ao jogo, {personagem.nome}!")

    # Criar uma criatura para a batalha
    criatura = Criatura("Goblin", vida=50, dano=10)

    while True:
        print("\nEscolha o que fazer:")
        print("1. Lutar contra a criatura")
        print("2. Sair do jogo")

        escolha = input("Digite 1 ou 2: ")

        if escolha == '1':
            ganhou = batalha(personagem, criatura)
            if ganhou:
                personagem.escolher_peculiaridade()  # Melhorar vida ou dano após vencer
        elif escolha == '2':
            print("Saindo do jogo... Até a próxima!")
            break
        else:
            print("Escolha inválida! Tente novamente.")

if __name__ == "__main__":
    main()
