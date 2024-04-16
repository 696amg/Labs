import pygame

pygame.init()

song_1 = '/Users/artem/Music/Music/Media.localized/Music/ASAP Rocky feat. Skepta/Unknown Album/Praise The Lord (Da Shine) (Sefon.Pro).mp3'
song_2 = '/Users/artem/Music/Music/Media.localized/Music/50 Cent/Unknown Album/Disco Inferno (Sefon.me).mp3'
song_3 = '/Users/artem/Downloads/Central Cee - Doja.mp3'

screen = pygame.display.set_mode((500, 410))
pygame.display.set_caption("player music")
clock = pygame.time.Clock()

pervii = pygame.mixer.music.load(song_1)#загрузка каждого трека
vtorii = pygame.mixer.music.load(song_2)
tretii = pygame.mixer.music.load(song_3)

mix = [song_2, song_1, song_3]
pygame.mixer.music.play(-1)

mixer = pygame.image.load('/Users/artem/Downloads/71f-F8oSRmL._AC_SL1500_.jpg')#картинка миксера
screen.blit(mixer, (0, 0))
PLAY = False#теперь цико чт
running = True
song = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PLAY = not PLAY
                if PLAY:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                song += 1
                if song == len(mix):
                    song = 0
                pygame.mixer.music.load(mix[song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                song -= 1
                if song == -1:
                    song = len(mix)-1
                pygame.mixer.music.load(mix[song])
                pygame.mixer.music.play()


    pygame.display.flip()
    clock.tick(60)