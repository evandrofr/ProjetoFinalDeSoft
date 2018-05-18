# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:51:28 2018

@author: Lenovo
"""

import pygame
import random
from firebase import firebase

firebase= firebase.FirebaseApplication('https://highscorejumper.firebaseio.com/',None)
if firebase.get('pasta',None) is None: #Cria o dicionario caso nao exista
    Highscore = {'highscore': 0}
else: #Abre o dicionario salvo no Firebase
    Highscore = firebase.get('pasta',None)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

width = 600
height = 600
size = 10
gravity = 1
scoremax = 0
#=========  CLASSES ==========

class Boneco (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
class Plataforma (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.platforms = [[400, 500, 0, 0]]

# ===============   INICIALIZAÇÃO   ===============
        
pygame.init()

relogio = pygame.time.Clock() #Cria relogio para definir FPS

tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
pygame.display.set_caption('Jumper') #Nome na aba

# carrega imagem de fundo
fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert()

boneco = Boneco("Imagens/Alien_80x80.png",width/2,height*(90/100),0,-1/10)
boneco_group = pygame.sprite.Group()
boneco_group.add(boneco)

plataforma_group = pygame.sprite.Group()

plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height*(95/100))
plataforma_group.add(plataforma)

plataforma_group2 = pygame.sprite.Group()


distx=400
disty=70

while plataforma.rect.y > disty:   #Adicionar plataformar aleatorias
    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,width),plataforma.rect.y-disty)
    plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,width),plataforma.rect.y-disty)
    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,width),plataforma.rect.y-disty)
    plataforma_group2.add(plataforma_quebra)
    plataforma_group.add(plataforma)
    plataforma_group.add(plataforma2)

score=0
myfont = pygame.font.SysFont("monospace", 16)
scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
tela.blit(scoretext, (5, 10))

# ===============   LOOPING PRINCIPAL   ===============
sair = True
while sair:
    for event in pygame.event.get(): #Controla eventos
       if event.type == pygame.QUIT: #Botao de fechar
           sair = False #Sai do loop 
       pressed_keys=pygame.key.get_pressed()
       if pressed_keys[pygame.K_LEFT]:
           boneco.vx = -3
       elif pressed_keys[pygame.K_RIGHT]:
           boneco.vx = +3
           
    if pygame.sprite.spritecollide(boneco,plataforma_group,False):   #pular encima das plat
        boneco.vy = -20
        scoremax += 15
 
    boneco.rect.y += boneco.vy      #fisica
    boneco.rect.x += boneco.vx*3.5
    
    boneco.vy += gravity
    
    
    #score = -boneco.rect.y + 600    #A janela do jogo tem como ponto mais baixo 600, e conforme\
                                    # o jogador sobe a pontuacao desce pois a borda superior eh o\
                                    # 0 e acima disso os numeros passam a ser negativos, \
                                    # devemos pensar em alguma forma de arrumar isso para\
                                    # ter uma pontuacao dependendo da altura.**
#    if score > scoremax:
#        scoremax = score
    if scoremax > Highscore['highscore']:
        Highscore['highscore'] = scoremax
        
    
#Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
    if boneco.rect.x > width:
        boneco.rect.x = 0
    if boneco.rect.x < 0:
        boneco.rect.x = width-size
    if boneco.rect.y > height:
        sair=False
    
    if pygame.sprite.spritecollide(boneco,plataforma_group2,True): #destroi plataforma que quebra
        boneco.vy = -20
        scoremax -= 10

    while plataforma.rect.y > disty:   #Adicionar plataformar aleatorias
        plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,800),plataforma.rect.y-disty)
        plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,800),plataforma.rect.y-disty)
        plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,800),plataforma.rect.y-disty)
        plataforma_group2.add(plataforma_quebra)
        plataforma_group.add(plataforma)
        plataforma_group.add(plataforma2)
        
    if boneco.rect.y <= height/4:
        boneco.rect.y += abs(boneco.vy)                                          
        for plataforma in plataforma_group:
            plataforma.rect.y += abs(boneco.vy)
        for plataforma in plataforma_group2:
            plataforma.rect.y += abs(boneco.vy)
        if plataforma.rect.y >= height:
            plataforma.kill()
    
#    while len(plataforma_group) < 10:
#        p = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,800),-boneco.rect.y-disty)
#        plataforma_group.add(p)
        
    tela.blit(fundo, (0, 0))
    scoretext = myfont.render("Score {0}, Highscore {1}".format(scoremax,Highscore['highscore']), 1, (0,0,0))
    tela.blit(scoretext, (5, 10))
    boneco_group.draw(tela)
    plataforma_group.draw(tela)
    plataforma_group2.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    relogio.tick(30) #Define FPS

firebase.patch('/pasta',Highscore)
pygame.quit() #Sai do jogo

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    