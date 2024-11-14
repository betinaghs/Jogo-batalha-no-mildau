import pygame, sys
from random import randint
pygame.init()

branco = (255,255,255)

#tela
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu inicial')
screen = pygame.display.set_mode((800, 600),0,32)
background = pygame.image.load('menu.png') #imagem tela inicial 
font1 = pygame.font.SysFont("Monospace", 60, bold=True) #JOGAR
font4 = pygame.font.SysFont("DejaVu Sans Mono", 15) 
font2 = pygame.font.SysFont("DejaVu Sans Mono", 30, bold=True) 
font3 = pygame.font.SysFont("DejaVu Sans Mono", 30) 
DEFALT_IMAGE_SIZE = (800, 600) 
background = pygame.transform.scale(background, DEFALT_IMAGE_SIZE) 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

somdefundo = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) #loop

#efeitos fazendeiro
pa = pygame.mixer.Sound('pa.wav') #som 1
tapa = pygame.mixer.Sound('tapa.mp3') #som 2
especial1 = pygame.mixer.Sound('especial1.mp3')
#afeitos espantalho
monstro1 = pygame.mixer.Sound('monstro1.mp3') #som 1
monstro2 = pygame.mixer.Sound('monstro2.mp3') #som 2
especial2 = pygame.mixer.Sound('especial2.mp3')


click = False

def main_menu():
    while True:
        screen.blit(background, (0,0))
        mx, my = pygame.mouse.get_pos()
        
        #BOTOES
        button_1 = pygame.Rect(300, 320, 200, 80) #jogar | lado - cima baixo - largura botao - altura botao  
        button_2 = pygame.Rect(614, 456, 106, 50) #opcoes
        #button_3 = pygame.Rect(60, 449, 125, 50) #sair
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        #if button_2.collidepoint((mx, my)): #jogar
            #if click:
                #options()
        if button_2.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (95, 163, 55), button_1)
        pygame.draw.rect(screen, (95, 163, 55), button_2)  
       # pygame.draw.rect(screen, (95, 163, 55), button_3)
        #TEXTO
        draw_text('JOGAR', font1, (222, 222, 18), screen, 310, 325) #lado (maior = + p direita) - cima baixo (maior = + baixo)
        draw_text('sair', font2, (222, 222, 18), screen,  630, 463)
        #draw_text('sair', font3, (222, 222, 18), screen, 85, 456)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    #jogo 
    largura_janela = 800  
    altura_janela = 600
    tela = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption('Batalha no Mildau')
    clock = pygame.time.Clock()               
                  
    #cores da barra do especial
    branco = (255,255,255)
    preto = (0,0,0)
    verde = (255,165,0) #laranja
    vermelho = (178,34,34) #vermelho


    def texto(msg, cor, tam, x, y):
        font = pygame.font.SysFont( 'Timesnewroman' , 27)
        texto1 = font.render(msg, True, cor)
        tela.blit(texto1, [x, y])

    fgExit = False

    cenario = pygame.image.load('cenario.png')
    fazendeiro = pygame.image.load('fazendeiro.png')
    fazendeiro2 = pygame.transform.scale(fazendeiro, (400, 400))
    espantalho = pygame.image.load('espantalho.png')
    espantalho2 = pygame.transform.scale(espantalho, (400, 400))

    vidafazendeiro = 20 #total de vida do jogador 01
    vidaespantalho = 20 #total de vida do jogador 02
    especialfazendeiro = 10 #contador do especial do jogador 01
    especialespantalho = 10 #contador do especial do jogador 01
    turno = randint (0, 1) #variável responsável para indicar a vez de cada jogador

    #loop do reset do game e botões de combate

    while not fgExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fgExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #K_r é o botão de reset
                    vidafazendeiro = 20
                    vidaespantalho = 20 
                    especialfazendeiro = 10
                    especialespantalho = 10
                    turno = randint (0, 1) #na primeira vez é sorteado a vez dos jogadores aleatoriamente usando o "randint (0, 1)"
                    pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                    texto("pontos de vida: "+str(vidafazendeiro), preto, 20, 10, altura_janela-30) #vida do jogador 1 #str()" que serve para transformar os valores de batalha que são calculados numericamente em texto a ser exibido na tela.
                    texto("pontos de vida: "+str(vidaespantalho), preto, 20, 500, altura_janela-30) #vida do jogador 2
                    pygame.display.update()

                    #JOGADOR 1 - FAZENDEIRO
            if event.type == pygame.KEYDOWN and vidafazendeiro >0 and vidaespantalho >0:            
                if event.key == pygame.K_1 and turno == 0: 
                #k_1 é a tecla do ataque basico
                #turno é responsável por fazer a contagem 0 e 1 para indicar a vez de cada jogador.
                    vidaespantalho = vidaespantalho - 1 #tira 1 da vida do jogador 2
                    especialfazendeiro = especialfazendeiro + 3 #da 3 pontos para carregar o especial do jogador 1
                    pa.play() #efeito especial
                    turno = 1
                    print (vidafazendeiro)
                if event.key == pygame.K_2 and turno == 0: #k_2 é a tecla do ataque carregado
                    vidaespantalho = vidaespantalho - 2 #tira 2 da vida do jogador 2
                    especialfazendeiro = especialfazendeiro + 1 #da 2 pontos para carregar o especial do jogador 1
                    tapa.play()
                    turno = 1
                    print (vidafazendeiro)
                if event.key == pygame.K_3 and especialfazendeiro >= 10 and turno == 0: 
                    vidaespantalho = vidaespantalho - randint(0, 5) #tira entre 0 e 5 pontos da vida do jogador 2
                    especialfazendeiro = especialfazendeiro - 9 
                    especial1.play()
                    turno = 1
                    print (vidafazendeiro)
                    #k_3 é a tecla do especial
                    #especial=maior ou igual a 10 pontos

                    #JOGADOR 2 - ESPANTALHO
                if event.key == pygame.K_8 and turno == 1: #k_8 é a tecla do ataque basico
                    vidafazendeiro = vidafazendeiro - 1 #tira 1 da vida do jogador 1
                    especialespantalho = especialespantalho + 3 #da 3 pontos para carregar o especial do jogador 2
                    monstro1.play()
                    turno = 0
                    print (vidaespantalho)
                if event.key == pygame.K_9 and turno == 1: #k_9 é a tecla do ataque carregado
                    vidafazendeiro = vidafazendeiro - 2  #tira 2 da vida do jogador 1
                    especialespantalho = especialespantalho + 1 #da 1 pontos para carregar o especial do jogador 2
                    monstro2.play()
                    turno = 0
                    print (vidaespantalho)
                if event.key == pygame.K_0 and especialespantalho >= 10 and turno == 1:
                    #k_0 é a tecla do especial
                    #especial=maior ou igual a 10 pontos,
                    vidafazendeiro = vidafazendeiro - randint(0, 5) #tira entre 0 e 5 pontos da vida do jogador 2
                    especialespantalho = especialespantalho - 9
                    especial2.play()
                    turno = 0
                    print (vidaespantalho)


    #loop dos pontos do placar de vida

            if vidafazendeiro >0 and vidaespantalho >0: #pontos de vida maior que 0
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                texto("Pontos de vida: "+str(vidafazendeiro), preto, 20, 10, altura_janela-30)
                texto("Pontos de vida: "+str(vidaespantalho), preto, 20, 500, altura_janela-30)
                pygame.display.update()
            if vidafazendeiro <= 0: #pontos de vida menor ou igual que 0
                print ('fazendeiro dead')
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40]) #desenho da área da escrita
                texto("Pontos de vida: morto", preto, 20, 10, altura_janela-30)
                texto("Pontos de vida: "+str(vidaespantalho), preto, 20, 500, altura_janela-30)
                pygame.display.update()
            if vidaespantalho <= 0: #pontos de vida menor ou igual que 0
                print ('espantalho dead')
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                texto("Pontos de vida: morto", preto, 20, 500, altura_janela-30)
                texto("Pontos de vida: "+str(vidafazendeiro), preto, 20, 10, altura_janela-30)
                pygame.display.update()


    #exibição de personagens/cenário, barra de especial e vez do jogador

        tela.blit(cenario,(0,0))
        tela.blit(fazendeiro2,(0,157))
        tela.blit(espantalho2, (400, 157))
        pygame.draw.rect(tela, branco, [0, 0, largura_janela, 40])
        pygame.draw.rect(tela, vermelho, [0, 0,((largura_janela/2)/10)*especialfazendeiro, 40])
        texto("ATAQUE ESPECIAL (3)", preto, 0, 10, 10)
        pygame.draw.rect(tela, branco, [largura_janela/2, 0, largura_janela/2, 40])
        pygame.draw.rect(tela, verde, [largura_janela/2, 0, ((largura_janela/2)/10)*especialespantalho, 40])
        texto("ATAQUE ESPECIAL (0)", preto, 0, (largura_janela/2)+10, 10)
        if turno == 0 and vidafazendeiro > 0 and vidaespantalho > 0:
            texto("vez do jogador 1", preto, 0, 120, 100) #escrita na tela em cada turno
        if turno == 1 and vidafazendeiro > 0 and vidaespantalho > 0:
            texto("vez do jogador 2", preto, 0, 550, 100) #escrita na tela em cada turno        
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

def exite():
    pygame.quit()
    sys.exit()


main_menu()