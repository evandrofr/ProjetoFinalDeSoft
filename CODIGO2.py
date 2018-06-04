# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:57:17 2018

@author: joao-
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
        pygame.mixer.music.load("DBSONG.mp3")
        pygame.mixer.music.play(-1)
    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
class Boneco2 (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        pygame.mixer.music.load("DBSONG.mp3")
        pygame.mixer.music.play(-1)
    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
class Monstro (pygame.sprite.Sprite):
    
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
    
    def __init__(self, arquivo_imagem,pos_x,pos_y,vel_x,vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.platforms = [[400, 500, 0, 0]]
        self.vx = vel_x
        self.vy = vel_y
        
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

#===============  FUNÇÕES AUXILIARES ===============
def texto(mensagem, cor):
    texto1 = myfont.render(mensagem, True, cor)
    tela.blit(texto1, [10, height/2])
# ===============   INICIALIZAÇÃO   ===============
        
pygame.init()
pygame.mixer.init()
som_pulo = pygame.mixer.Sound("phaseJump2.ogg")

relogio = pygame.time.Clock() #Cria relogio para definir FPS

tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
pygame.display.set_caption('Jumper') #Nome na aba

fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert() # carrega imagem de fundo

boneco = Boneco("Imagens/Alien_azul.png",width/2,height*(90/100),0,-1/10)
boneco_group = pygame.sprite.Group()
boneco_group.add(boneco)

boneco2 = Boneco2("Imagens/Alien_verde.png",width/2,height*(90/100),0,-1/10)
boneco2_group = pygame.sprite.Group()
boneco2_group.add(boneco2)

distx=200
disty = 50

plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height*(95/100),0,0)
plataforma_group = pygame.sprite.Group()
plataforma_group.add(plataforma)

plataforma_group2 = pygame.sprite.Group()

plataformaMovel = Plataforma("Imagens/Plataforma_Movel.png",0,800,0,0)
plataformaMovel_group=pygame.sprite.Group()
plataformaMovel_group.add(plataformaMovel)

monstro = Monstro("Imagens/Monstro.png",0,800,0,0)
monstro_group=pygame.sprite.Group()
monstro_group.add(monstro)

while plataforma.rect.y > disty:   #Adicionar plataformar aleatorias
    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,width),plataforma.rect.y-disty,0,0)
    plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,width),plataforma.rect.y-disty,0,0)
    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,width),plataforma.rect.y-disty,0,0)
    plataforma_group2.add(plataforma_quebra)
    plataforma_group.add(plataforma)
    plataforma_group.add(plataforma2)
    
score=0
myfont = pygame.font.SysFont("monospace", 16)
scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
tela.blit(scoretext, (5, 10))

# ===============   LOOPING MENU   ===============

menu = True
while menu:
    
    for event in pygame.event.get(): #Controla eventos
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[pygame.K_c]:
            menu = False
        if pressed_keys[pygame.K_q]:
            pygame.quit()
    
    tela.blit(fundo, (0, 0))
    texto("Utilize as setas para mover o boneco!Clique C para iniciar!", black)
    scoretext = myfont.render("Score {0}, Highscore {1}".format(scoremax,Highscore['highscore']), 1, (0,0,0))
    tela.blit(scoretext, (5, 10))
    boneco_group.draw(tela)
    boneco2_group.draw(tela)
    plataforma_group.draw(tela)
    plataforma_group2.draw(tela)
    plataformaMovel_group.draw(tela) 
    pygame.display.flip()      #coloca a tela na janela
    pygame.display.update()
    relogio.tick(30)
        
# ===============   LOOPING PRINCIPAL   ===============
delta = 5
delta2= 7
tick_counter=0
tempo1=30*1     #fps*segundos
tempo2=30*15
tempo3=30*30 


sair = True
while sair:

    for event in pygame.event.get(): #Controla eventos
       if event.type == pygame.QUIT: #Botao de fechar
           sair = False #Sai do loop 
    #Movimentação
       pressed_keys=pygame.key.get_pressed()
       boneco.vx = 0
           
       if pressed_keys[pygame.K_LEFT]:
           boneco.vx = -3

       if pressed_keys[pygame.K_RIGHT]:
           boneco.vx = +3
           
       pressed_keys=pygame.key.get_pressed()
       boneco2.vx = 0
           
       if pressed_keys[pygame.K_a]:
           boneco2.vx = -3

       if pressed_keys[pygame.K_d]:
           boneco2.vx = +3           

    boneco.rect.y += boneco.vy      #fisica
    boneco.rect.x += boneco.vx*3.5
    boneco2.rect.y += boneco2.vy      #fisica
    boneco2.rect.x += boneco2.vx*3.5
    
    boneco.vy += gravity
    boneco2.vy += gravity

    if scoremax > Highscore['highscore']:
        Highscore['highscore'] = scoremax
        
        #Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
    if boneco.rect.x > width:
        boneco.rect.x = 0
    if boneco.rect.x < 0:
        boneco.rect.x = width-size
    if boneco.rect.y > height:
        boneco.kill()
                
    if boneco2.rect.x > width:
        boneco2.rect.x = 0
    if boneco2.rect.x < 0:
        boneco2.rect.x = width-size
    if boneco2.rect.y > height:
        boneco2.kill()
        
    if boneco.vy > 1:
        if pygame.sprite.spritecollide(boneco,plataforma_group2,True): #destroi plataforma que quebra
            if boneco.rect.y<height:
                som_pulo.play()
                boneco.vy = -20
                scoremax += 15
        if pygame.sprite.spritecollide(boneco,plataforma_group,False):   #pular encima das plat
            if boneco.rect.y<height:
                som_pulo.play()
                boneco.vy = -20
                scoremax += 10
            
    if boneco2.vy > 1:
        if pygame.sprite.spritecollide(boneco2,plataforma_group2,True): #destroi plataforma que quebra
            if boneco2.rect.y<height:
                som_pulo.play()
                boneco2.vy = -20
                scoremax += 15
        if pygame.sprite.spritecollide(boneco2,plataforma_group,False):   #pular encima das plat
            if boneco2.rect.y<height:
                som_pulo.play()
                boneco2.vy = -20
                scoremax += 10
                
    #==================Aumento da dificuldade conforme o jogo passa ===========  
          
    if tick_counter > tempo1 and tick_counter < tempo2:            #tempo 1
        plataformaMovel.rect.x += delta
        if plataformaMovel.rect.x > 499:
            delta = -5
        elif plataformaMovel.rect.x<0:
            delta=5
        chance=random.randrange(0,1000)
        if chance >=997:
            plataformaMovel = Plataforma("Imagens/Plataforma_Movel.png",0,boneco.rect.y-200,0,0)
            plataformaMovel_group.add(plataformaMovel)
            plataformaMovel.rect.x += delta
        else:
            while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma_group2.add(plataforma_quebra)
                plataforma_group.add(plataforma)
                plataforma_group.add(plataforma2)
        
    if tick_counter > tempo2 and tick_counter < tempo3:       #tempo 2
        plataformaMovel.rect.x += delta
        if plataformaMovel.rect.x > 499:
            delta = -10
        elif plataformaMovel.rect.x<0:
            delta=10
        chance=random.randrange(0,1000)
        if chance >=996:
            plataformaMovel = Plataforma("Imagens/Plataforma_Movel.png",0,boneco.rect.y-200,0,0)
            plataformaMovel_group.add(plataformaMovel)
            plataformaMovel.rect.x += delta
        else:
            while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma_group2.add(plataforma_quebra)
                plataforma_group.add(plataforma)
                plataforma_group.add(plataforma2)
                
    if tick_counter>tempo3:
        monstro.rect.x+=delta2
        if monstro.rect.x > 529:
            delta2 = -7
        elif monstro.rect.x<0:
            delta2=7 
        chance=random.randrange(0,1000)
        if chance >=994:
            monstro = Monstro("Imagens/Monstro.png",random.randrange(0,520),0,0,0)
            monstro_group.add(monstro)
            monstro.rect.x+=delta2
        plataformaMovel.rect.x += delta
        if plataformaMovel.rect.x > 499:
            delta = -10
        elif plataformaMovel.rect.x<0:
            delta=10
        chance2=random.randrange(0,1000)
        if chance2 >=997:
            plataformaMovel = Plataforma("Imagens/Plataforma_Movel.png",0,boneco.rect.y-200,0,0)
            plataformaMovel_group.add(plataformaMovel)
            plataformaMovel.rect.x += delta
        else:
            while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty,0,0)
                plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,500),plataforma.rect.y-disty,0,0)
                plataforma_group2.add(plataforma_quebra)
                plataforma_group.add(plataforma)
    
    pygame.sprite.spritecollide(plataformaMovel,plataforma_group,True)
    pygame.sprite.spritecollide(plataformaMovel,plataforma_group2,True)
    pygame.sprite.spritecollide(monstro,plataforma_group,True)
    pygame.sprite.spritecollide(monstro,plataforma_group2,True)
    
    if boneco.vy>1:
        if pygame.sprite.spritecollide(boneco,monstro_group,True):
            som_pulo.play()
            boneco.vy = -20
            scoremax += 30    
    else:
        if pygame.sprite.spritecollide(monstro,boneco_group,True):
            sair=True

    if boneco.rect.y<boneco2.rect.y:    
        if boneco.rect.y <= height-250:
            boneco.rect.y += abs(boneco.vy)                                          
            for plataforma in plataforma_group:
                plataforma.rect.y += abs(boneco.vy)
            for plataforma in plataforma_group2:
                plataforma.rect.y += abs(boneco.vy)
            if plataforma.rect.y >= height:
                plataforma.kill()
            for plataformaMovel in plataformaMovel_group:
                plataformaMovel.rect.y += abs(boneco.vy)
            if plataformaMovel.rect.y >= height:
                plataformaMovel.kill()
            for monstro in monstro_group:
                monstro.rect.y += abs(boneco.vy)
            if monstro.rect.y >= height:
                monstro.kill()

    else:
        if boneco2.rect.y <= height-250:
            boneco2.rect.y += abs(boneco2.vy)                                          
            for plataforma in plataforma_group:
                plataforma.rect.y += abs(boneco2.vy)
            for plataforma in plataforma_group2:
                plataforma.rect.y += abs(boneco2.vy)
            if plataforma.rect.y >= height:
                plataforma.kill()
            for plataformaMovel in plataformaMovel_group:
                plataformaMovel.rect.y += abs(boneco2.vy)
            if plataformaMovel.rect.y >= height:
                plataformaMovel.kill()
            for monstro in monstro_group:
                monstro.rect.y += abs(boneco.vy)
            if monstro.rect.y >= height:
                monstro.kill()
   
    tela.blit(fundo, (0, 0))
    scoretext = myfont.render("Score {0}, Highscore {1}".format(tick_counter,Highscore['highscore']), 1, (0,0,0))
    tela.blit(scoretext, (5, 10))
    boneco_group.draw(tela)
    boneco2_group.draw(tela)
    plataforma_group.draw(tela)
    plataforma_group2.draw(tela)
    plataformaMovel_group.draw(tela)
    monstro_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    relogio.tick(30) #Define FPS
    tick_counter+=1

firebase.patch('/pasta',Highscore)
pygame.quit() #Sai do jogo