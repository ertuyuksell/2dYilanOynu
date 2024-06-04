import pygame
import time
import random

pygame.init()

# Renkler
beyaz=(255,255,255)
siyah=(0,0,0)
sarı=(238,232,170)
kirmizi=(213,50,80)
magenta=(139,101,139)
acıkSarı=(250,250,210)

# Ekran boyutları
yükseklik=1000
en=1500

ekran = pygame.display.set_mode((en, yükseklik))
pygame.display.set_caption('Yılan Oyunu')

saat = pygame.time.Clock()

yilanBoyutu = 10
yilanHizi = 20

fontStil = pygame.font.SysFont("Times New Roman", 50)
skorFont = pygame.font.SysFont("Times New Roman", 30)

def yilan(yilanBoyutu, yilanListesi):
    for x in yilanListesi:
        pygame.draw.rect(ekran, siyah, [x[0], x[1], yilanBoyutu, yilanBoyutu])

def mesaj(msj, renk):
    mesj = fontStil.render(msj, True, renk)
    ekran.blit(mesj, [en / 6, yükseklik / 3])

def oyunDongusu():
    oyunBitti= False
    oyunKapandi = False

    x1 = en / 2
    y1 = yükseklik / 2

    x1Degisim = 0
    y1Degisim = 0

    yilanListesi = []
    yilanUzunlugu = 1

    yedikceX = round(random.randrange(0, en - yilanBoyutu) / 10.0) * 10.0
    yedikceY = round(random.randrange(0, yükseklik - yilanBoyutu) / 10.0) * 10.0

    while not oyunBitti:

        while oyunKapandi == True:
            ekran.fill(acıkSarı)
            mesaj("Kaybettiniz! Q-Quit veya C-Continue", kirmizi)
            pygame.display.update()

            for olay in pygame.event.get():
                if olay.type == pygame.KEYDOWN:
                    if olay.key == pygame.K_q:
                        oyunBitti = True
                        oyunKapandi = False
                    if olay.key == pygame.K_c:
                        oyunDongusu()

        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                oyunBitti = True
            if olay.type == pygame.KEYDOWN:
                if olay.key == pygame.K_LEFT:
                    x1Degisim = -yilanBoyutu
                    y1Degisim = 0
                elif olay.key == pygame.K_RIGHT:
                    x1Degisim = yilanBoyutu
                    y1Degisim = 0
                elif olay.key == pygame.K_UP:
                    y1Degisim = -yilanBoyutu
                    x1Degisim = 0
                elif olay.key == pygame.K_DOWN:
                    y1Degisim = yilanBoyutu
                    x1Degisim = 0

        if x1 >= en or x1 < 0 or y1 >= yükseklik or y1 < 0:
            oyunKapandi = True
        x1 += x1Degisim
        y1 += y1Degisim
        ekran.fill(acıkSarı)
        pygame.draw.rect(ekran, magenta, [yedikceX, yedikceY, yilanBoyutu, yilanBoyutu])
        yilanBasi= []
        yilanBasi.append(x1)
        yilanBasi.append(y1)
        yilanListesi.append(yilanBasi)
        if len(yilanListesi) > yilanUzunlugu:
            del yilanListesi[0]

        for x in yilanListesi[:-1]:
            if x == yilanBasi:
                oyunKapandi = True

        yilan(yilanBoyutu, yilanListesi)

        pygame.display.update()

        if x1 == yedikceX and y1 == yedikceY:
            yedikceX = round(random.randrange(0, en - yilanBoyutu) / 10.0) * 10.0
            yedikceY = round(random.randrange(0, yükseklik - yilanBoyutu) / 10.0) * 10.0
            yilanUzunlugu += 1

        saat.tick(yilanHizi)

    pygame.quit()
    quit()

oyunDongusu()