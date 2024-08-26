import random
import time

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
Clock = pygame.time.Clock()
running =  True

music = pygame.mixer.music.load("game-music-loop-7-145285.mp3")
pygame.mixer.music.play(-1)

Diff = random.randint(380, 410)
Gravity = 0.24
Speed = 0.025
Score = 0

I1 = pygame.transform.scale(pygame.image.load("Bird.png"),
                            (24, 17))
IX = 200
IY = 250

Up = pygame.transform.scale(pygame.image.load("UpPipe.png"),
                            (140, 305))
UX = 1000
UY = random.randint(-100, 50)

Down = pygame.transform.scale(pygame.image.load("DownPipe.png"),
                              (140, 305))
DX = UX
DY = UY + Diff

F1 = pygame.transform.scale(pygame.image.load("Floor.png"),
                              (1000, 400))
F1Rect = F1.get_rect(center=(400, 600))

Font1 = pygame.font.Font("MouldyCheeseRegular-WyMWG.ttf", 40)

while running:

    IRect = I1.get_rect(center=(IX, IY))
    UpRect = Up.get_rect(center=(UX, UY))
    DownRect = Down.get_rect(center=(DX, DY))

    T1 = Font1.render(f"Score: {Score}", True, "black")
    T1Rect = T1.get_rect(center=(400, 480))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(I1, IRect)
    screen.blit(Up, UpRect)
    screen.blit(Down, DownRect)
    screen.blit(F1, F1Rect)
    screen.blit(T1, T1Rect)

    UX -= 5
    if UX <= -40:
        Diff = random.randint(380, 410)
        UX = 1000
        DX = UX
        UY = random.randint(-60, 50)
        DY = UY + Diff
        Score += 1
        print(Score)
        pygame.mixer.Sound("success-1-6297.mp3").play()
    DX = UX

    keys = pygame.key.get_pressed()

    IY += Gravity
    Gravity += Speed
    Speed += 0.001

    if keys[pygame.K_UP]:
        IY -= 3
        Gravity = 0.2
        Speed = 0.05

    if IRect.colliderect(F1Rect) or IRect.colliderect(UpRect) or IRect.colliderect(DownRect):
        time.sleep(1)
        running = False

    pygame.display.update()
    Clock.tick(100)