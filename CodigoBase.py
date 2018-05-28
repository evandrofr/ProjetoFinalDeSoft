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
    
pygame.init()
pygame.mixer.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

width = 800
height = 600
size = 10
gravity = 1
scoremax = 0

distx = 400
disty = 50

fonte_menu = pygame.font.SysFont("comicsansms", 40)
fonte_nome = pygame.font.SysFont("comicsansms", 72)

jogar = fonte_menu.render("Jogar",1,black)
sair = fonte_menu.render("Sair",1,black)
menu = fonte_menu.render("Menu",1,black)    

jogar_selecionado = fonte_menu.render("Jogar",1,red)
sair_selecionado = fonte_menu.render("Sair",1,red)
menu_selecionado = fonte_menu.render("Menu",1,red)

nome_jogo = fonte_nome.render("JUMPER!",1,black)
nome_gameover = fonte_nome.render("GAME OVER!",1,black)

som_pulo = pygame.mixer.Sound("phaseJump2.ogg")


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
    
class Plataforma (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.platforms = [[400, 500, 0, 0]]

#===============  FUNÇÕES AUXILIARES ===============
def texto(mensagem, cor):
    texto1 = myfont.render(mensagem, True, cor)
    tela.blit(texto1, [width/6, height/2])
#    pygame.display.flip()
    


# ===============   INICIALIZAÇÃO   ===============
        
#pygame.init()
#pygame.mixer.init()
##pygame.Font.init()
#som_pulo = pygame.mixer.Sound("phaseJump2.ogg")
#
#relogio = pygame.time.Clock() #Cria relogio para definir FPS
#
#tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
#pygame.display.set_caption('Jumper') #Nome na aba
#
## carrega imagem de  
#fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert()
#
#boneco = Boneco("Imagens/Alien_80x80.png",width/2,height*(90/100),0,-1/10)
#boneco_group = pygame.sprite.Group()
#boneco_group.add(boneco)
#
#plataforma_group = pygame.sprite.Group()
#
#plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height*(95/100))
#plataforma_group.add(plataforma)
#
#plataforma_group2 = pygame.sprite.Group()
#
#
#distx=400
#disty = 50
#
#while plataforma.rect.y > disty:   #Adicionar plataformar aleatorias
#    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,width),plataforma.rect.y-disty)
#    plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,width),plataforma.rect.y-disty)
#    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,width),plataforma.rect.y-disty)
#    plataforma_group2.add(plataforma_quebra)
#    plataforma_group.add(plataforma)
#    plataforma_group.add(plataforma2)
#
#score=0
#myfont = pygame.font.SysFont("monospace", 16)
#scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
#tela.blit(scoretext, (5, 10))

# ===============   LOOPING MENU   ===============

#menu = True
#while menu:
#    
#    for event in pygame.event.get(): #Controla eventos
#        pressed_keys=pygame.key.get_pressed()
#        if pressed_keys[pygame.K_c]:
#            menu = False
#        if pressed_keys[pygame.K_q]:
#            pygame.quit()
#    tela.blit(fundo, (0, 0))
#    texto("Jumper! Utilize as setas para mover o boneco!Clique C para iniciar ou Clique Q para sair!", red)
#    scoretext = myfont.render("Score {0}, Highscore {1}".format(scoremax,Highscore['highscore']), 1, (0,0,0))
#    tela.blit(scoretext, (5, 10))
#    boneco_group.draw(tela)
#    plataforma_group.draw(tela)
#    plataforma_group2.draw(tela)
#    pygame.display.flip()      #coloca a tela na janela
#    pygame.display.update()
#    relogio.tick(30)


#Opçoes do menu
loopgeral = True
menuloop = True
while loopgeral:
    
    mn = menu_selecionado
    js = jogar_selecionado
    sa = sair
     
    selec = 0
    #variavel para o movimento do cursor
    start=[280,250]
    
    relogio = pygame.time.Clock() #Cria relogio para definir FPS
    tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
    pygame.display.set_caption('Jumper') #Nome na aba
    
    # carrega imagem de  
    fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert()
    
    boneco = Boneco("Imagens/Alien_80x80.png",width/2,height*(90/100),0,-1/10)
    boneco_group = pygame.sprite.Group()
    boneco_group.add(boneco)
    
    plataforma_group = pygame.sprite.Group()
    
    plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height*(95/100))
    plataforma_group.add(plataforma)
    
    plataforma_group2 = pygame.sprite.Group()
    
    
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

    selec = 1
    while menuloop:      
        
        for event in pygame.event.get():
            pressed_keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT: 
                pygame.quit()
                
            elif event.type==pygame.KEYDOWN:
                if pressed_keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    
                elif js==jogar_selecionado and pressed_keys[pygame.K_DOWN]:
                    js=jogar
                    sa=sair_selecionado
                    selec=2
                    start=[280,350]
            
                elif js==jogar_selecionado and pressed_keys[pygame.K_UP]:
                    js=jogar
                    sa=sair_selecionado
                    selec=2
                    start=[280,350]
            
            
                elif sa==sair_selecionado and pressed_keys[pygame.K_DOWN]:
                    js=jogar_selecionado
                    sa=sair
                    selec=1
                    start=[280,250]
            
                elif sa==sair_selecionado and pressed_keys[pygame.K_UP]:
                    js=jogar_selecionado
                    sa=sair
                    selec=1
                    start=[280,250]
            
                elif selec==1 and event.key==pygame.K_RETURN:
                    menuloop = False
                    loop = True
                    loopgeral = True
                    gameover = False
                    
                elif selec==2 and event.key==pygame.K_RETURN:
                    menuloop = False
                    loop = False
                    loopgeral = False
                    gameover = False
            
            
            tela.blit(fundo, (0, 0))
            tela.blit(js, [350,250])
            tela.blit(sa, [350,350])
            tela.blit(nome_jogo, [270,100])
            tela.blit(pygame.image.load("cursor.png"), start)
            boneco_group.draw(tela)
            pygame.display.flip()      #coloca a tela na janela
            pygame.display.update()
            relogio.tick(30)
    
    # ===============   LOOPING PRINCIPAL   ===============
    
    
    while loop:
    
        for event in pygame.event.get(): #Controla eventos
           if event.type == pygame.QUIT: #Botao de fechar
               loop = False #Sai do loop 
               loopgeral = False
               
        #Movimentação
           pressed_keys=pygame.key.get_pressed()
           boneco.vx = 0
               
           if pressed_keys[pygame.K_LEFT]:
               boneco.vx = -3
    
           if pressed_keys[pygame.K_RIGHT]:
               boneco.vx = +3
               
         
            
     
        boneco.rect.y += boneco.vy      #fisica
        boneco.rect.x += boneco.vx*3.5
        boneco.vy += gravity
    
        
        
    #    if score > scoremax:
    #        scoremax = score
        if scoremax > Highscore['highscore']:
            Highscore['highscore'] = scoremax
            
        
    #Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
        if boneco.rect.x > width:
            boneco.rect.x = 0
        if boneco.rect.x < 0:
            boneco.rect.x = width-size
        if boneco.rect.bottom > height + 30:
            loop=False
            gameover = True
            
            
            
        if boneco.vy > 1:
            if pygame.sprite.spritecollide(boneco,plataforma_group2,True): #destroi plataforma que quebra
                som_pulo.play()
                boneco.vy = -20
                scoremax += 15
            if pygame.sprite.spritecollide(boneco,plataforma_group,False):   #pular encima das plat
                som_pulo.play()
                boneco.vy = -20
                scoremax += 10
    
        while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
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
        
    select = 1
    while gameover:
       
       for event in pygame.event.get():
            pressed_keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT: 
                pygame.quit()
                
            elif event.type==pygame.KEYDOWN:
                if pressed_keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    
                elif mn == menu_selecionado and pressed_keys[pygame.K_DOWN]:
                    mn = menu
                    sa = sair_selecionado
                    select = 2
                    start = [280,350]
            
                elif mn == menu_selecionado and pressed_keys[pygame.K_UP]:
                    mn = menu
                    sa = sair_selecionado
                    select = 2
                    start = [280,350]
            
            
                elif sa == sair_selecionado and pressed_keys[pygame.K_DOWN]:
                    mn = menu_selecionado
                    sa = sair
                    select = 1
                    start = [280,250]
            
                elif sa == sair_selecionado and pressed_keys[pygame.K_UP]:
                    mn = menu_selecionado
                    sa = sair
                    select = 1
                    start = [280,250]
            
                elif selec==1 and event.key==pygame.K_RETURN:
                    gameover = False
                    menuloop = True
                    loop = False
                    loopgeral = True
                    
                elif selec==2 and event.key==pygame.K_RETURN:
                    menuloop = False
                    gameover = False
                    loopgeral = False
                    loop = False
                    
            
            
    #        mov += 1
            tela.blit(fundo, (0, 0))
            tela.blit(mn, [350,250])
            tela.blit(sa, [350,350])
            tela.blit(nome_gameover, [250,100])
            tela.blit(pygame.image.load("cursor.png"), start)
            boneco_group.draw(tela)
            pygame.display.flip()      #coloca a tela na janela
            pygame.display.update()
            relogio.tick(30) 





firebase.patch('/pasta',Highscore)
pygame.quit() #Sai do jogo

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    