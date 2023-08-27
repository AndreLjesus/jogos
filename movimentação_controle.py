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

x_player, y_player = 160, 90
velocidade=1
controle_x, controle_y = velocidade, 0

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
      if event.button == 11:
        if controle_y == velocidade:
          pass
        else:
          controle_y = -velocidade
          controle_x = 0

      elif event.button == 12:
        if controle_y == -velocidade:
          pass
        else:
          controle_y = velocidade
          controle_x = 0

      elif event.button == 13:
        if controle_x == velocidade:
          pass
        else:
          controle_x = -velocidade
          controle_y = 0

      elif event.button == 14:
        if controle_x == -velocidade:
          pass
        else:
          controle_x = velocidade
          controle_y = 0

  x_player = x_player + controle_x
  y_player = y_player + controle_y
        

  #player
  player = pygame.draw.rect(tela, (0, 0, 255), (x_player, y_player, 16, 16))
  #movimentação player teclado
  if pygame.key.get_pressed()[K_d]:
    x_player += 1
  if pygame.key.get_pressed()[K_a]:
    x_player -= 1
  if pygame.key.get_pressed()[K_w]:
    y_player -= 1
  if pygame.key.get_pressed()[K_s]:
    y_player += 1

  pygame.display.update()
