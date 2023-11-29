import pygame
import random
import time

pygame.init()

WIDTH = 1550
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DEADLY TARGET')

largura_zumbi = 50
altura_zumbi = 50
background = pygame.image.load('fundo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (largura_zumbi, altura_zumbi))
mira_img = pygame.image.load('Mira.png').convert_alpha()
mira_img = pygame.transform.scale(mira_img, (80, 80))
score_font = pygame.font.Font('HelpMe.ttf', 50)

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.set_volume(0.4)

som_zumbis = pygame.mixer.Sound('zumbis.mp3')
som_zumbis.set_volume(0.2)

som_bala = pygame.mixer.Sound('bala.mp3')
som_bala.set_volume(0.1)

som_grito = pygame.mixer.Sound("grito.mp3")
som_grito.set_volume(0.4)

class Zumbi(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - largura_zumbi) 
        self.rect.y = 450
        self.speedx = -0.4
        self.speedy = 0.8

        self.tamanho_original = (largura_zumbi, altura_zumbi)
    
    def reset(self):

        self.rect.x = random.randint(0, WIDTH - 2*largura_zumbi)
        self.rect.y = 450
    
    def update(self):

        tamanho_aumento = self.rect.y/2
        novo_tamanho = (int(self.tamanho_original[0] + tamanho_aumento), int(self.tamanho_original[1] + tamanho_aumento))
        self.image = pygame.transform.scale(zumbi_img, novo_tamanho)
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Mira(pygame.sprite.Sprite):

    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect(center = (WIDTH/2 ,  HEIGHT/2))

    def update(self):

        self.rect.center = pygame.mouse.get_pos()

def mensagem(texto, cor, posicao):
    fonte = pygame.font.Font('HelpMe.ttf',35)
    texto = fonte.render(texto, True, cor)
    window.blit(texto, posicao)

def mensagem2(texto, cor, posicao):
    fonte = pygame.font.Font('HelpMe.ttf',50)
    texto = fonte.render(texto, True, cor)
    window.blit(texto, posicao)

def mensagem3(texto, cor, posicao):
    fonte = pygame.font.Font('HelpMe.ttf',80)
    texto = fonte.render(texto, True, cor)
    window.blit(texto, posicao)

def mensagem4(texto, cor, posicao):
    fonte = pygame.font.Font('HelpMe.ttf',30)
    texto = fonte.render(texto, True, cor)
    window.blit(texto, posicao)

def tela_inicial():
    inicio = True

    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicio = False

        window.fill((0, 0, 0))
        mensagem3("DEADLY TARGET", (255,0,0), (450,50))
        mensagem("VOCE ACORDA DE MADRUGADA E PERCEBE QUE O", (255, 255, 255),(320, 200))
        mensagem(" APOCALIPSE QUE TANTO FALAVAM DE FATO ERA REAL.", (255, 255, 255), (270, 280))
        mensagem("VOCE PEGA SUA ARMA E SAI CORRENDO",(255, 255, 255),(390, 380))
        mensagem("EM DIREÇAO AO QUINTAL AO OUVIR O SOM DOS ZUMBIS.",(255, 255, 255), (220, 460))
        mensagem2("VOCE TEM O QUE E NECESSARIO PARA SALVAR TODOS?",(255,0,0), (45,560))
        mensagem4("DICA: OS ZUMBIS SO MORREM COM TIROS NA CABEÇA",(255,0,0),(340,630))
        mensagem("Pressione ENTER para começar", (255, 255, 255),(450, 700))
        pygame.display.update()

def end_game_bom():
    fim_bom = True

    while fim_bom:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicio = True
                    main()
                else:
                    pygame.quit()
                    quit()
        window.fill((0, 0, 0))
        mensagem4("Tendo enfrentado hordas interminaveis de zumbis e demonstrado uma mira impecavel,",(255,255,255),(20,50))
        mensagem4("voce conseguiu sobreviver a noite apocaliptica. O amanhecer revela silhuetas",(255,255,255),(70,100))
        mensagem4("desaparecendo ao longe, enquanto o som distante de sirenes indica a chegada dos",(255,255,255),(30,150))
        mensagem4("socorristas. Voce permanece de pe, exausto, mas triunfante. Seu quintal, outrora",(255,255,255),(30,200))
        mensagem4("invadido pelos mortos-vivos, agora esta calmo. A cidade, um cenario de caos,",(255,255,255),(60,250))
        mensagem4("começa a mostrar sinais de recuperaçao. Os sobreviventes começam a emergir dos",(255,255,255),(30,300))
        mensagem4("esconderijos, agradecendo a coragem e habilidade que você demonstrou.",(255,255,255),(100,350))
        mensagem4("As autoridades chegam para restabelecer a ordem, e voce, o heroi improvavel,",(255,255,255),(50,400))
        mensagem4("e reconhecido por sua valentia. A comunidade se une para reconstruir,",(255,255,255),(120,450))
        mensagem4("prometendo não esquecer os eventos dessa noite terrivel. Voce olha para o",(255,255,255),(100,500))
        mensagem4("horizonte, sabendo que o perigo pode não ter totalmente desaparecido, mas",(255,255,255),(50,550))
        mensagem4("confiante de que sua determinação e destreza foram fundamentais para salvar vidas.",(255,255,255),(0,600))
        mensagem2("O FIM?", (255,0,0), (680,650))
        mensagem4("PRESSIONE ENTER PARA JOGAR DE NOVO OU QUALQUER OUTRA TELA PARA SAIR DO JOGO",(255,0,0), (60,720))

        pygame.display.update()

def end_game_ruim():
    fim_ruim = True

    while fim_ruim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicio = True
                    main()
                else:
                    pygame.quit()
                    quit()
        window.fill((0, 0, 0))
        mensagem4("A noite se estendeu, implacavel, testando sua coragem e habilidade. Mas, apesar",(255,255,255),(50,50))
        mensagem4("de seus esforços, a invasao zumbi provou ser insuperavel. O som de passos",(255,255,255),(70,100))
        mensagem4("arrastados se intensifica, indicando que os mortos-vivos continuam a se multiplicar.",(255,255,255),(0,150))
        mensagem4("Exausto e desgastado, voce e cercado por uma mare interminavel de zumbis famintos. ",(255,255,255),(5,200))
        mensagem4("A escuridão engole seu último suspiro de esperança, enquanto as criaturas se",(255,255,255),(60,250))
        mensagem4("aproximam, determinadas a reivindicar mais uma vitima. Seu destino e selado pela",(255,255,255),(55,300))
        mensagem4("mordida de um zumbi, marcando o fim de sua resistencia. A visao embaça enquanto",(255,255,255),(20,350))
        mensagem4("as forças da escuridão triunfam sobre sua luta solitária. Seu nome, agora esquecido,",(255,255,255),(0,400))
        mensagem4("e apenas mais um eco perdido em um mundo tomado pelos mortos. O apocalipse",(255,255,255),(30,450))
        mensagem4("zumbi nao concedeu perdao, e sua jornada chegou a um fim sombrio. Seu sacrificio",(255,255,255),(20,500))
        mensagem4("nao foi suficiente para salvar aqueles que amava, e agora, você se junta às fileiras",(255,255,255),(10,550))
        mensagem4("dos que caminham sem proposito, uma sombra de sua antiga humanidade.",(255,255,255),(100,600))
        mensagem2("O FIM?", (255,0,0), (680,650))
        mensagem4("PRESSIONE ENTER PARA JOGAR DE NOVO OU QUALQUER OUTRA TELA PARA SAIR DO JOGO",(255,0,0), (60,720))
       


        pygame.display.update()   

def main():
    game = True
    clock = pygame.time.Clock()
    FPS = 30

    all_sprites = pygame.sprite.Group()
    all_zumbis = pygame.sprite.Group()
    for i in range(3):
        zumbi = Zumbi(zumbi_img)
        all_sprites.add(zumbi)
        all_zumbis.add(zumbi)
    mira = Mira(mira_img)
    all_sprites.add(mira)

    score = 0
    zumbi_added = False

    pygame.mixer.music.play(loops=-1)
    som_zumbis.play(loops=-1)

    while game:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game = False
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                som_bala.play()
                for zumbi in all_zumbis:
                    area_colisao_ampliada = zumbi.rect.inflate(100, 100)
                    if area_colisao_ampliada.collidepoint(pygame.mouse.get_pos()):
                        zumbi.reset()
                        score += 100

        if score != 0 and score % 2000 == 0 and not zumbi_added:
            novo_zumbi = Zumbi(zumbi_img)
            all_sprites.add(novo_zumbi)
            all_zumbis.add(novo_zumbi)
            zumbi_added = True

            nova_mira = Mira(mira_img)
            all_sprites.add(nova_mira)

        if score % 2000 != 0:
            zumbi_added = False

        all_sprites.update()

        if score >= 100:
            game = False
            end_game_bom()

        for zumbi in all_zumbis:
            if zumbi.rect.bottom >= HEIGHT:
                som_grito.play()
                game = False


        window.blit(background, (0, 0))
        all_sprites.draw(window)

        text_surface = score_font.render("SCORE:{:06d}".format(score), True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()

tela_inicial()
main()
end_game_ruim()