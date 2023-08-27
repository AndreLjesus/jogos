import pygame
from pygame.locals import *
from sys import exit

#inicalização do joystick
pygame.joystick.init()
joysticks = [
  pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())
]
#print caso tenha um controle conectado
for js in joysticks:
  print(js)



#tela
largura, altura = 320, 180
tela = pygame.display.set_mode([largura, altura])

#config_parede
x_parede = largura

#configurações do player
pulo_min= altura-32-16
pulo_max = altura-30-16-60
y_player = 132
velocidade=1.5
controle_y = 0

#configuração do fps do jogo
fps = pygame.time.Clock()

pygame.init()

while True:

  #velocidade do fps
  fps.tick(60)

  #limpar a tela
  tela.fill((0, 0, 0))

  #exit
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()

    #Print de botão caso controle conectado
    elif event.type == pygame.JOYBUTTONDOWN:
      if event.button == 0:
        velocidade = 1
        controle_y = -velocidade

  #limite pulo
  if y_player <= pulo_max:
    controle_y = velocidade

  #altura minima
  if y_player > 132:
    y_player = pulo_min
    controle_y = 0
    velocidade = 0

  #player
  y_player = y_player + controle_y
  player = pygame.draw.rect(tela, (0, 0, 255), (160, y_player, 16, 16))

  #chão
  chao = pygame.draw.rect(tela, (0,255,0), (0, altura-32, largura, 32))

  x_parede -=1
  parede = pygame.draw.rect(tela, (100,100,0), (x_parede, altura-64, 16,32))
  if x_parede < 0:
    x_parede = largura

  pygame.display.update()
