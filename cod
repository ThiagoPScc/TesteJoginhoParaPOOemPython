import random

# classe jogador
class Jogador:

  def __init__ (self,vida,dano,level,classe):
    self.vida = vida
    self.dano = dano
    self.level = level
    self.classe = classe

  def darDano(self,inimigo):
    inimigo.vidaIni -= self.dano

  def mostrarDados(self):
    print(self.vida,self.dano)

  def curar(self):
    print("vida antes da cura:", self.vida)
    self.vida += 3 *self.level
    print("vida após a cura:", self.vida)

  def subirNivel(self):
    self.vida = self.vida * random.randint(2,3) + self.level
    self.dano = self.dano * random.randint(2,3) + self.level
    self.bonus()
    self.mostrarDados()

  def escolherClasse(self):
    desicao = int(input("escolha sua classe: \n 1.Guerreiro - vida:20 e ataque:10 \n 2.Mago - vida:10 e ataque:20 \n 3.Tanque - vida:30 e ataque:5 \n"))
    if desicao == 1:
      self.vida = 20
      self.dano = 10
      self.level = 1
      self.classe = "guerreiro"
    elif desicao == 2:
      self.vida = 10
      self.dano = 20
      self.level = 1
      self.classe = "Mago"
    elif desicao == 3:
      self.vida = 30
      self.dano = 5
      self.level = 1
      self.classe = "guerreiro"
    else :
      self.vida = 15
      self.dano = 15
      self.level = 1
      self.classe = "Andrailho"

    self.mostrarDados()


  def bonus(self):
      bonusEscolha = int(input("escolha seu buff: \n 1. +5 de dano ou 2. + 10 de vida"))

      if bonusEscolha == 1:
          self.dano +=5
      else:
          self.vida +=10
#classe inimigo

class Inimigo:

    def __init__ (self, vidaIni, danoIni):
        self.vidaIni = vidaIni
        self.danoIni = danoIni

    def darDanoIni(self, jogador):
        jogador.vida = jogador.vida - self.danoIni

    def mostrarDadosIni(self):
        print(self.vidaIni, self.danoIni)

    def criarInimigo(self, mapa):
        if mapa.area == 5:
            print("este é o boss")
            valor = random.randint(1, 10) * 3
        else:
            valor = random.randint(1, 5)

        self.vidaIni = valor * mapa.nivel
        self.danoIni = valor * mapa.nivel

        print("vida:", self.vidaIni, "ataque:", self.danoIni)


#classe mapa

class Mapa:
  def __init__(self,nivel,local,area):
    self.nivel = nivel
    self.local = local
    self.area = area

  def escolherLocal(self):
    escolha = int(input("escolha o local: \n 1.floresta \n 2.lago \n 3.casarão \n"))

    if escolha == 1:
      self.local = "floresta"
      print(self.local)

    elif escolha == 2:
      self.local = "lago"
      print(self.local)

    elif escolha == 3:
      self.local = "casarão"
      print(self.local)
    else:
      self.local = "masmorra"
      self.nivel += 3
      print(self.local)



  def mudarMapa(self,jogador):
    self.area += 1
    if self.area == 6:
      self.area = 1
      self.nivel += 1
      jogador.subirNivel()
      jogador.mostrarDados()
      print("parabens, você mudou de área, escolha a próxima")
      self.escolherLocal()
    else:

      print("você avança")



  def combate(self,inimigo,jogador):

    print("um inimigo apareceu")

    vivo = True
    inimigoVivo = True
    inimigo.criarInimigo(self)

    while vivo == True and inimigoVivo == True:
      decisaoCombate = int(input("escolha sua ação: \n 1.atacar \n 2.curar \n"))
      if decisaoCombate == 1:
        inimigo.darDanoIni(jogador)
        jogador.darDano(inimigo)
      else:
        jogador.curar()
        inimigo.darDanoIni(jogador)

      if inimigo.vidaIni > 0:
        print("o inimigo ainda está vivo")
        inimigo.mostrarDadosIni()
      else:
        inimigoVivo = False

      if jogador.vida > 0:
        print(jogador.vida)
      else:
        vivo = False
        print("perdeu")
        break

    self.mudarMapa(jogador)



#jogo em sí
j1 = Jogador(0,0,0,"vazio")
m1 = Mapa(1,"vazio",1)
I1 = Inimigo(1,1)

j1.escolherClasse()
m1.escolherLocal()


while j1.vida > 0:
  caminho = int(input("1.caminho seguro \n2.caminho perigoso \n3.Mostrar Status \n4.Sair \n1"))
  if caminho == 1:

    print("caminho escolhido: seguro")
    j1.curar()
  elif caminho == 2:

    print("caminho escolhido: perigoso")
    m1.combate(I1,j1)
  elif caminho == 3:
    j1.mostrarDados()
  elif caminho == 4:

    break


print("área final:",m1.nivel)
print("Obrigado por jogar")


