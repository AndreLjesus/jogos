import pygame
from sys import exit
from pygame.locals import *

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for js in joysticks:
  print(js)

#tela
largura, altura = 320, 180
tela = pygame.display.set_mode([largura, altura])

x_player, y_player = 160, 90

#configuração do fps do jogo
fps = pygame.time.Clock()

pygame.init()

while True:

  #velocidade do fps
  fps.tick(30)

  #limpar a tela
  tela.fill((0,0,0))

  for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()

  #player
  player = pygame.draw.rect(tela, (0,0,255), (x_player,y_player,16,16))
  if pygame.key.get_pressed()[K_d]:
    x_player +=1
  if pygame.key.get_pressed()[K_a]:
    x_player -=1
  if pygame.key.get_pressed()[K_w]:
    y_player-=1
  if pygame.key.get_pressed()[K_s]:
    y_player+=1
  
  
  pygame.display.update()
