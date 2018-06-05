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
    
#=========  CLASSES ==========
    
class Plataforma (pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.platforms = [[400, 500, 0, 0]]
        
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

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
    
class PlataformaM (pygame.sprite.Sprite):
    
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
    tela.blit(texto1, [width/6, height/2])
#    pygame.display.flip()
    
# ===============   INICIALIZAÇÃO E VARIAVIEIS  ===============
    
pygame.init()
pygame.mixer.init()

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
scoremax2 = 0

delta = 5
delta2 = 7
tick_counter = 0
fps = 30
tempo1 =fps*1     #fps*segundos
tempo2 = fps*15
tempo3 = fps*30 

distx = 400
disty = 50

start_pos1 = [200,260]
start_pos2 = [200,360]
start_pos3 = [200,460]

fonte_menu = pygame.font.SysFont("comicsansms", 40)
fonte_nome = pygame.font.SysFont("comicsansms", 72)
myfont = pygame.font.SysFont("monospace", 16)

jogar = fonte_menu.render("Jogar",1,black)
jogar2 = fonte_menu.render("Jogar em 2",1,black)
sair = fonte_menu.render("Sair",1,black)
menu = fonte_menu.render("Menu",1,black)    

jogar_selecionado = fonte_menu.render("Jogar",1,red)
jogar2_selecionado = fonte_menu.render("Jogar em 2",1,red)
sair_selecionado = fonte_menu.render("Sair",1,red)
menu_selecionado = fonte_menu.render("Menu",1,red)

nome_jogo = fonte_nome.render("JUMPER!",1,black)
nome_gameover = fonte_nome.render("GAME OVER!",1,black)

som_pulo = pygame.mixer.Sound("phaseJump2.ogg")

relogio = pygame.time.Clock() #Cria relogio para definir FPS
tela = pygame.display.set_mode((width,height),0,32) #Tamanho da tela
pygame.display.set_caption('Jumper') #Nome na aba

# carrega imagem de  
fundo = pygame.image.load("Imagens/Fundo_800x600.png").convert()

boneco = Boneco("Imagens/Alien_azul.png",width/2,height*(90/100),0,-1/10)
boneco_group = pygame.sprite.Group()
boneco_group.add(boneco)

boneco2 = Boneco2("Imagens/Alien_verde.png",width/2,height*(90/100),0,-1/10)
boneco2_group = pygame.sprite.Group()
boneco2_group.add(boneco2)

distx=200
disty = 50

plataforma = Plataforma("Imagens/Plataforma_verde.png",width/2,height*(95/100))
plataforma_group = pygame.sprite.Group()
plataforma_group.add(plataforma)

plataforma_group2 = pygame.sprite.Group()

plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",0,800,0,0)
plataformaMovel_group=pygame.sprite.Group()
plataformaMovel_group.add(plataformaMovel)

monstro = Monstro("Imagens/Monstro.png",0,800,0,0)
monstro_group=pygame.sprite.Group()
monstro_group.add(monstro)


# ===============   lOOPS   ===============

#Opçoes do menu
loopgeral = True
menuloop = True
while loopgeral:
    
    mn = menu_selecionado
    js = jogar_selecionado
    js2 = jogar2
    sa = sair
    scoremax = 0
    scoremax2 = 0
     
    #variavel para o movimento do cursor
    start = start_pos1
    
    
    while plataforma.rect.y > disty:   #Adicionar plataformar aleatorias
        plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,width-50),plataforma.rect.y-disty)
        plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,width-50),plataforma.rect.y-disty)
        plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,width-50),plataforma.rect.y-disty)
        plataforma_group2.add(plataforma_quebra)
        plataforma_group.add(plataforma)
        plataforma_group.add(plataforma2)
    
#    score=0
#    scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
#    tela.blit(scoretext, (5, 10))

    selec = 1
    while menuloop:      
        
        for event in pygame.event.get():
            pressed_keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT: 
                pygame.quit()
                
            elif event.type==pygame.KEYDOWN:
                if pressed_keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    
                elif js == jogar_selecionado and pressed_keys[pygame.K_DOWN]:
                    js = jogar
                    js2 = jogar2_selecionado
                    sa = sair
                    selec = 2
                    start = start_pos2
            
                elif js == jogar_selecionado and pressed_keys[pygame.K_UP]:
                    js = jogar
                    js2 = jogar2
                    sa = sair_selecionado
                    selec = 3
                    start = start_pos3
                    
                elif js2 == jogar2_selecionado and pressed_keys[pygame.K_DOWN]:
                    js = jogar
                    js2 = jogar2
                    sa = sair_selecionado
                    selec = 3
                    start = start_pos3
                
                elif js2 == jogar2_selecionado and pressed_keys[pygame.K_UP]:
                    js = jogar_selecionado
                    js2 = jogar2
                    sa = sair
                    selec = 1
                    start = start_pos1
            
            
                elif sa==sair_selecionado and pressed_keys[pygame.K_DOWN]:
                    js = jogar_selecionado
                    js2 = jogar2
                    sa = sair
                    selec = 1
                    start = start_pos1
            
                elif sa == sair_selecionado and pressed_keys[pygame.K_UP]:
                    js = jogar
                    js2 = jogar2_selecionado
                    sa = sair
                    selec = 2
                    start = start_pos2
            
                elif selec == 1 and event.key==pygame.K_RETURN:
                    menuloop = False
                    loopjogo = True
                    loopjogo2 = False
                    loopgeral = True
                    gameover = False
                
                elif selec == 2 and event.key==pygame.K_RETURN:
                    menuloop = False
                    loopjogo = False
                    loopjogo2 = True
                    loopgeral = True
                    gameover = False
                    
                elif selec == 3 and event.key==pygame.K_RETURN:
                    menuloop = False
                    loopjogo = False
                    loopjogo2 = False
                    loopgeral = False
                    gameover = False
            
            
            tela.blit(fundo, (0, 0))
            tela.blit(js, [250,250])
            tela.blit(js2, [250,350])
            tela.blit(sa, [250,450])
            tela.blit(nome_jogo, [150,100])
            tela.blit(pygame.image.load("cursor.png"), start)
            boneco_group.draw(tela)
            pygame.display.flip()      #coloca a tela na janela
            pygame.display.update()
            relogio.tick(fps)
    
    # ===============   LOOPING PRINCIPAL   ===============
    
    
    while loopjogo:
    
        for event in pygame.event.get(): #Controla eventos
           if event.type == pygame.QUIT: #Botao de fechar
               loopjogo = False #Sai do loop 
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
    
        if scoremax > Highscore['highscore']:
            Highscore['highscore'] = scoremax
            
    #Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
        if boneco.rect.x > width:
            boneco.rect.x = 0
        if boneco.rect.x < 0:
            boneco.rect.x = width-size
        if boneco.rect.bottom > height + 30:
            loopjogo = False
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
            if pygame.sprite.spritecollide(boneco,plataformaMovel_group,False):
                som_pulo.play()
                boneco.vy = -20
                scoremax += 20
                
                
    
        while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
            plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,800),plataforma.rect.y-disty)
            plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,800),plataforma.rect.y-disty)
            plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,800),plataforma.rect.y-disty)
            plataforma_group2.add(plataforma_quebra)
            plataforma_group.add(plataforma)
            plataforma_group.add(plataforma2)
            
        if boneco.rect.y <= height - 300:
            boneco.rect.y += abs(boneco.vy)                                          
            for plataforma in plataforma_group:
                plataforma.rect.y += abs(boneco.vy)
            for plataforma in plataforma_group2:
                plataforma.rect.y += abs(boneco.vy)
            for monstro in monstro_group:
                monstro.rect.y += abs(boneco.vy)
            for plataformamovel in plataformaMovel_group:
                plataformamovel.rect.y += abs(boneco.vy)
            if monstro.rect.y >= height:
                monstro.kill()
            if plataformaMovel.rect.y >= height:
                plataformaMovel.kill()
            if plataforma.rect.y >= height:
                plataforma.kill()
                
                #==================Aumento da dificuldade conforme o jogo passa ===========  
                
        if tick_counter > tempo1 and tick_counter < tempo2:            #tempo 1
            plataformaMovel.rect.x += delta
        if plataformaMovel.rect.x > 499:
            delta = -5
        elif plataformaMovel.rect.x<0:
            delta=5
        chance=random.randrange(0,1000)
        if chance >=997:
            plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",random.randint(100,width-100),boneco.rect.y- 200,0,0)
            plataformaMovel_group.add(plataformaMovel)
            plataformaMovel.rect.x += delta
        else:
            while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty)
                plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty)
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
                plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",random.randint(100,width-100),boneco.rect.y -200,0,0)
                plataformaMovel_group.add(plataformaMovel)
                plataformaMovel.rect.x += delta
            else:
                while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty)
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
                plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",0,boneco.rect.y-200,0,0)
                plataformaMovel_group.add(plataformaMovel)
                plataformaMovel.rect.x += delta
            else:
                while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,500),plataforma.rect.y-disty)
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
                loopjogo = False
                gameover = True
        
        
        tela.blit(fundo, (0, 0))
        scoretext = myfont.render("Tempo {0}, Score {1}, Highscore {2}".format(tick_counter,scoremax,Highscore['highscore']), 1, (0,0,0))
        tela.blit(scoretext, (5, 10))
        boneco_group.draw(tela)
        plataforma_group.draw(tela)
        plataforma_group2.draw(tela)
        plataformaMovel_group.draw(tela)
        monstro_group.draw(tela)
        pygame.display.update()      #coloca a tela na janela
        relogio.tick(fps) #Define FPS
        tick_counter += 1
        
        
        
       # ===============   LOOPING PRINCIPAL   ===============
    
    
    while loopjogo2:
    
        for event in pygame.event.get(): #Controla eventos
           if event.type == pygame.QUIT: #Botao de fechar
               loopjogo2 = False #Sai do loop 
               loopgeral = False
               
        #Movimentação
           pressed_keys=pygame.key.get_pressed()
           boneco.vx = 0
           boneco2.vx = 0
               
           if pressed_keys[pygame.K_LEFT]:
               boneco.vx = -3
        
           if pressed_keys[pygame.K_RIGHT]:
               boneco.vx = +3
           
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
    
            
    #Feito para o objeto "atravessar" as bordas e reaparecer do outro lado
#        if boneco.rect.x > width:
#            boneco.rect.x = 0
#        if boneco.rect.x < 0:
#            boneco.rect.x = width-size
#        if boneco.rect.bottom > height + 30:
#            boneco.kill()
#            loopjogo2 = False
#            gameover = True
#            
#        if boneco2.rect.x > width:
#            boneco2.rect.x = 0
#        if boneco2.rect.x < 0:
#            boneco2.rect.x = width-size
#        if boneco2.rect.bottom > height+30:
#            boneco2.kill()
#            loopjogo2 = False
#            gameover = True
    
        if boneco2.rect.bottom > height+30:
            boneco2.kill()
            loopjogo2 = False
            gameover = True
        if boneco.rect.bottom > height+30:
            boneco.kill()
            loopjogo2 = False
            gameover = True
        
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
            if pygame.sprite.spritecollide(boneco,plataformaMovel_group,False):
                if boneco.rect.y<height:
                    som_pulo.play()
                    boneco.vy = -20
                    scoremax += 20
                
        if boneco2.vy > 1:
            if pygame.sprite.spritecollide(boneco2,plataforma_group2,True): #destroi plataforma que quebra
                if boneco2.rect.y<height:
                    som_pulo.play()
                    boneco2.vy = -20
                    scoremax2 += 15
            if pygame.sprite.spritecollide(boneco2,plataforma_group,False):   #pular encima das plat
                if boneco2.rect.y<height:
                    som_pulo.play()
                    boneco2.vy = -20
                    scoremax2 += 10
            if pygame.sprite.spritecollide(boneco2,plataformaMovel_group,False):
                if boneco2.rect.y<height:
                    som_pulo.play()
                    boneco.vy = -20
                    scoremax2 += 20
                
                
    
        while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
            plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,800),plataforma.rect.y-disty)
            plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,800),plataforma.rect.y-disty)
            plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,800),plataforma.rect.y-disty)
            plataforma_group2.add(plataforma_quebra)
            plataforma_group.add(plataforma)
            plataforma_group.add(plataforma2)
            
        if boneco.rect.y <= height - 250:
            boneco.rect.y += abs(boneco.vy)                                          
            for plataforma in plataforma_group:
                plataforma.rect.y += abs(boneco.vy)
            for plataforma in plataforma_group2:
                plataforma.rect.y += abs(boneco.vy)
            for monstro in monstro_group:
                monstro.rect.y += abs(boneco.vy)
            for plataformamovel in plataformaMovel_group:
                plataformamovel.rect.y += abs(boneco.vy)
            if monstro.rect.y >= height:
                monstro.kill()
            if plataformaMovel.rect.y >= height:
                plataformaMovel.kill()
            if plataforma.rect.y >= height:
                plataforma.kill()
                
                #==================Aumento da dificuldade conforme o jogo passa ===========  
                
        if tick_counter > tempo1 and tick_counter < tempo2:            #tempo 1
            plataformaMovel.rect.x += delta
        if plataformaMovel.rect.x > 499:
            delta = -5
        elif plataformaMovel.rect.x<0:
            delta=5
        chance=random.randrange(0,1000)
        if chance >=997:
            plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",random.randint(100,width-100),boneco.rect.y - 200,0,0)
            plataformaMovel_group.add(plataformaMovel)
            plataformaMovel.rect.x += delta
        else:
            while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty)
                plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty)
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
                plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",random.randint(100,width-100),boneco.rect.y,0,0)
                plataformaMovel_group.add(plataformaMovel)
                plataformaMovel.rect.x += delta
            else:
                while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma2 = Plataforma("Imagens/Plataforma_verde.png",random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,600),plataforma.rect.y-disty)
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
                plataformaMovel = PlataformaM("Imagens/Plataforma_Movel.png",0,boneco.rect.y-200,0,0)
                plataformaMovel_group.add(plataformaMovel)
                plataformaMovel.rect.x += delta
            else:
                while plataforma.rect.y > disty :   #Adicionar plataformar aleatorias
                    plataforma = Plataforma("Imagens/Plataforma_verde.png",plataforma.rect.x + random.randrange(0,600),plataforma.rect.y-disty)
                    plataforma_quebra=Plataforma("Imagens/Plataforma_Quebra.png",random.randrange(0,500),plataforma.rect.y-disty)
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
                loopjogo2 = False
                gameover = True
        
        
        tela.blit(fundo, (0, 0))
        scoretext1 = myfont.render("Tempo {0}, ScoreBlue {1}".format(tick_counter,scoremax), 1, (0,0,0))
        scoretext2 = myfont.render("ScoreGreen {0}".format(scoremax2), 1, (0,0,0))
        tela.blit(scoretext1, (5, 10))
        tela.blit(scoretext2, (450, 10))
        boneco_group.draw(tela)
        boneco2_group.draw(tela)
        plataforma_group.draw(tela)
        plataforma_group2.draw(tela)
        plataformaMovel_group.draw(tela)
        monstro_group.draw(tela)
        pygame.display.update()      #coloca a tela na janela
        relogio.tick(fps) #Define FPS
        tick_counter += 0.5
        
        
    select = 1
    start = start_pos1
    while gameover:
       
       for event in pygame.event.get():
            pressed_keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT: 
                pygame.quit()
                
            if event.type==pygame.KEYDOWN:
                if pressed_keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    
                elif mn == menu_selecionado and pressed_keys[pygame.K_DOWN]:
                    mn = menu
                    sa = sair_selecionado
                    select = 2
                    start = start_pos2
            
                elif mn == menu_selecionado and pressed_keys[pygame.K_UP]:
                    mn = menu
                    sa = sair_selecionado
                    select = 2
                    start = start_pos2
            
                elif sa == sair_selecionado and pressed_keys[pygame.K_DOWN]:
                    mn = menu_selecionado
                    sa = sair
                    select = 1
                    start = start_pos1
            
                elif sa == sair_selecionado and pressed_keys[pygame.K_UP]:
                    mn = menu_selecionado
                    sa = sair
                    select = 1
                    start = start_pos1
            
                elif selec==1 and event.key==pygame.K_RETURN:
                    gameover = False
                    menuloop = True
                    loopjogo = False
                    loopgeral = True
                    loopjogo2 = False
                    
                elif selec==2 and event.key==pygame.K_RETURN:
                    menuloop = False
                    gameover = False
                    loopgeral = False
                    loopjogo = False
                    loopjogo2 = False
                    
                    
            tela.blit(fundo, (0, 0))
            tela.blit(mn, [250,250])
            tela.blit(sa, [250,350])
            tela.blit(nome_gameover, [120,100])
            tela.blit(pygame.image.load("cursor.png"), start)
            pygame.display.flip()      #coloca a tela na janela
            pygame.display.update()
            relogio.tick(fps) 


firebase.patch('/pasta',Highscore)
pygame.quit() #Sai do jogo


    
    
    
    
    
    
    
    
    
    
    
    
