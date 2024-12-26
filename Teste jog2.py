#Esse joguinho foi feito para ser jogado no Google Colab
import ipywidgets as widgets
from IPython.display import display
import random
import time
from IPython.display import clear_output
class Personagem:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.ouro = 0
        self.xp = 0
        self.level = 1
        self.classe = None


    #classes
    def escolher_classe(self,Criatura):
      print("escolha sua classe")
      buttonEscolhaMago = widgets.Button(description="Mago")
      print("vida = 30 e dano = 20")
      def mago(b):
        self.vida= 30
        self.dano= 20
        self.classe = "Mago"
        print(f"\nBem-vindo ao jogo, {self.nome}, você é um,{self.classe}, habilidoso!")
        !clear
        self.escolha_caminho(Criatura)
      buttonEscolhaMago.on_click(mago)
      display(buttonEscolhaMago)

      buttonEscolhaGuerreiro = widgets.Button(description="Guerreiro")
      print("vida = 45 e dano = 5")
      def Guerreiro(b):
        self.vida= 45
        self.dano= 5
        self.classe = "Guerreiro"
        print(f"\nBem-vindo ao jogo, {self.nome}, você é um,{self.classe}, habilidoso!")
        !clear
        self.escolha_caminho(Criatura)
      buttonEscolhaGuerreiro.on_click(Guerreiro)
      display(buttonEscolhaGuerreiro)

      buttonEscolhaArqueiro = widgets.Button(description="Arqueiro")
      print("vida = 25 e dano = 25")
      def Arqueiro(b):
        self.vida= 25
        self.dano= 25
        self.classe = "Arqueiro"
        print(f"\nBem-vindo ao jogo, {self.nome}, você é um,{self.classe}, habilidoso!")
        !clear
        self.escolha_caminho(Criatura)
      buttonEscolhaArqueiro.on_click(Arqueiro)
      display(buttonEscolhaArqueiro)




      #caminhos

    def escolha_caminho(self,Criatura):
      
      print("escolha seu caminho")
      buttonEscolhaCaminho1 = widgets.Button(description="batalhar")
      def batalhar(b):
        Criatura.CriarInimigo(self)
      buttonEscolhaCaminho1.on_click(batalhar)
      display(buttonEscolhaCaminho1)


      buttonEscolhaCaminho2 = widgets.Button(description="Loja")
      def loja(b):
          print("Bem-vindo à loja!")
          print("Escolha o que deseja comprar:")
          
          # Criação dos botões
          buttonSair = widgets.Button(description="Sair (batalhar)")
          buttonVida = widgets.Button(description="Comprar +5 Vida (20 Ouro)")
          buttonDano = widgets.Button(description="Comprar +5 Dano (100 Ouro)")
          buttonMaxVida = widgets.Button(description="Comprar +50 Vida Máxima (100 Ouro)")
          
          # Funções associadas aos botões
          def sair_loja(b):
              print("Obrigado por visitar a loja.")
              Criatura.CriarInimigo(self)
              
          def comprar_vida(b):
              if self.ouro >= 20:
                  self.vida += 5
                  self.ouro -= 20
                  print("Você comprou +5 pontos de vida!")
              else:
                  print("Ouro insuficiente!")
              
          def comprar_dano(b):
              if self.ouro >= 100:
                  self.dano += 5
                  self.ouro -= 100
                  print("Você comprou +5 de dano!")
              else:
                  print("Ouro insuficiente!")
              
          def comprar_max_vida(b):
              if self.ouro >= 100:
                  self.vida += 50
                  self.ouro -= 100
                  print("Você comprou +50 pontos de vida máxima!")
              else:
                  print("Ouro insuficiente!")
          
  
          buttonSair.on_click(sair_loja)
          buttonVida.on_click(comprar_vida)
          buttonDano.on_click(comprar_dano)
          buttonMaxVida.on_click(comprar_max_vida)
              
              # Exibe os botões
          display(buttonSair, buttonVida, buttonDano, buttonMaxVida)

      # Exibe o botão para entrar na loja
      buttonEscolhaCaminho2.on_click(loja)
      display(buttonEscolhaCaminho2)

      




      buttonEscolhaCaminho3 = widgets.Button(description="Mostrar status")
      def mostrarStatus(b):
          clear_output()
          print(f"Nome: {self.nome}")
          print(f"Vida: {self.vida}")
          print(f"Dano: {self.dano}")
          print(f"Ouro: {self.ouro}")
          print(f"XP: {self.xp}")
          print(f"Level: {self.level}")
          self.escolha_caminho(Criatura)

      buttonEscolhaCaminho3.on_click(mostrarStatus)
      display(buttonEscolhaCaminho3)


      buttonEscolhaCaminho4 = widgets.Button(description="sair")
      def sair(b):
        print("obrigado por jogar")
        #exit()
        return
      buttonEscolhaCaminho4.on_click(sair)
      display(buttonEscolhaCaminho4)



    #combate
    def atacar(self, criatura):
        dano_caused = self.dano
        criatura.vida -= dano_caused
        print(f"{self.nome} atacou a criatura e causou {dano_caused} de dano!")

    def receber_ataque(self, dano_received):
        self.vida -= dano_received
        print(f"{self.nome} recebeu {dano_received} de dano!")

    def curar(self, quantidade):
        self.vida += quantidade 
        print(f"{self.nome} recuperou {quantidade} de vida!")

    def ganhar_ouro(self, quantidade):
        self.ouro += quantidade * self.level
        print(f"{self.nome} ganhou {quantidade} de ouro!")

    def ganhar_xp(self, quantidade):
        valorParaSubirDeLevel = 100 + (self.level * 1.5)
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")
        if self.xp >= valorParaSubirDeLevel:
            self.level_up()

    def level_up(self):
        self.xp = 0
        self.level += 1
        self.dano += 5
        self.vida += 10
        print(f"vida: {self.vida}")
        print(f"dano: {self.dano}")
        print(f"{self.nome} subiu de nível! Agora está no nível {self.level}!")
        self.escolher_peculiaridade()

    def escolher_peculiaridade(self):
        print("\nEscolha o que melhorar:")
        buttonDano = widgets.Button(description="Aumentar +5 Dano")
        buttonMaxVida = widgets.Button(description="Aumentar +50 Vida Máxima")
        def aumentar_dano(b):
            self.dano += 5
            print("Você escolheu aumentar +5 de dano!")
              
        def aumentar_vida_max(b):
            self.vida += 50
            print("Você escolheu aumentar +50 de vida máxima!")


        buttonDano.on_click(aumentar_dano)
        buttonMaxVida.on_click(aumentar_vida_max)
        display(buttonDano, buttonMaxVida)


#Monstro
class Criatura:
    def __init__(self):
        self.nome = "nome"
        self.vida = 0
        self.dano = 0
        self.xp = 0
        self.valor = 0

    def CriarInimigo(self,Personagem):
      inimigo = random.randint(1,3)
      if inimigo == 1:
          self.nome = "Goblin"
          vidamaxima = 20 * Personagem.level
          danomaximo = 5 * Personagem.level
          self.vida = random.randint(20, vidamaxima)
          self.dano = random.randint(5, danomaximo)
          self.xp = 10 * Personagem.level
          self.valor = 10 * Personagem.level
      elif inimigo == 2:
          self.nome = "Orc"
          vidamaxima = 30 * Personagem.level
          danomaximo = 5 * Personagem.level
          self.vida = random.randint(30, vidamaxima)
          self.dano = random.randint(10, danomaximo)
          self.xp = 30 * Personagem.level
          self.valor = 15 * Personagem.level
      elif inimigo == 3:
          self.nome = "Dragao"
          vidamaxima = 50 * Personagem.level
          danomaximo = 5 * Personagem.level
          self.vida = random.randint(50, vidamaxima)
          self.dano = random.randint(15, danomaximo)
          self.xp = 50 * Personagem.level
          self.valor = 20 * Personagem.level
      print(f"Você encontrou um {self.nome} com {self.vida} de vida e {self.dano} de dano!")
      self.batalha(Personagem)



    def atacar(self, personagem):
        dano_caused = random.randint(0, self.dano)
        personagem.receber_ataque(dano_caused)
        print(f"A criatura atacou e causou {dano_caused} de dano!")

    def batalha(self,personagem):
      while personagem.vida > 0 and self.vida > 0:
        # O jogador ataca
        personagem.atacar(self)
        time.sleep(1)  # Pausa para dar mais ritmo ao jogo

        # A criatura ataca de volta
        if self.vida > 0:
            self.atacar(personagem)
            time.sleep(1)  # Pausa para dar mais ritmo ao jogo

        # Mostra o status após cada turno
        print(f"Vida do {personagem.nome}: {personagem.vida}")
        print(f"Vida da Criatura: {self.vida}")
        print("-" * 20)

        # Checando se alguém morreu
        if personagem.vida <= 0:
            print(f"{personagem.nome} foi derrotado!")
            print(f"veja seus status finais: \n {personagem.nome}\n {personagem.classe}\n {personagem.level} \n {personagem.ouro}")
            return False  # Jogador perdeu
        elif self.vida <= 0:
            clear_output()
            print(f"{personagem.nome} derrotou a criatura!")
            personagem.ganhar_ouro(random.randint(5, 20))
            personagem.ganhar_xp(random.randint(10, 50))
            personagem.escolha_caminho(self)
            return True  # Jogador venceu



def main():
    print("________                                             __________          __  .__                    ")
    print("\\______ \\  __ __  ____    ____   ____  ____   ____   \\______   \\___.__._/  |_|  |__   ____   ____  ")
    print(" |    |  \\|  |  \\/    \\  / ___\\_/ __ \\/  _ \\ /    \\   |     ___<   |  |\\   __\\  |  \\/  _ \\ /    \\ ")
    print(" |    `   \\  |  /   |  \\/ /_/  >  ___(  <_> )   |  \\  |    |    \\___  | |  | |   Y  (  <_> )   |  \\")
    print("/_______  /____/|___|  /\\___  / \\___  >____/|___|  /  |____|    / ____| |__| |___|  /\\____/|___|  /")
    print("        \\/           \//_____/      \\/           \\/             \\/                \\/            \\/ ")
    print("                                                                                                    ")

    print("Bem-vindo ao jogo de RPG!")
    menu = input("1.Sair \n 2.Jogar \n")
    if menu == "1":
      print("obrigado por jogar")
      #exit()
      return
    else:
      nome = input("Digite o nome do seu personagem: ")
      personagem = Personagem(nome, 0,0)
      criatura = Criatura()
      personagem.escolher_classe(criatura)




if __name__ == "__main__":
    main()
