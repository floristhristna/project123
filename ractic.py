import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
#background
background = pygame.image.load('imgonline-com-ua-pixelizationyrGUycBVbnME.jpg')
# екран
pygame.display.set_caption("Space Villains")
icon = pygame.image.load('001-icon-6685200.png')
pygame.display.set_icon(icon)
# player літачок
playerImg = pygame.image.load('spaceship.png')
playerX = 350
playerY = 480
playerX_change = 0
# player інопрешеленець
enemyImg = pygame.image.load('002-ufo.png')
enemyX = random.randint(0, 750)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 30
# fire
bulletImg = pygame.image.load('fire.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "готово"  #не видно на екрані


def player(X, Y):
    screen.blit(playerImg, (X, Y))



def enemy(X, Y):
    screen.blit(enemyImg, (X, Y))
def fire_bulled(X, Y):
    global bulled_state
    bullet_state = "fire"# буде видно
    screen.blit(bulletImg, (X+15, Y+10))


# цикл
running = True
clock = pygame.time.Clock()
while running:
    # rgb
    screen.fill((10, 10, 100))
    #bground
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # шоб вікно не закривалось і не скакало
            running = False

        # keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                 bulletX = playerX
                 fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # якщо більше то він почне рухатись сам по ординаті

    # для кораблика
    playerX += playerX_change
    # шоб не вилітав за межі
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    # для енемі
    enemyX += enemyX_change

    # шоб не вилітав за межі
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change  # Переміщуємо ворога вниз тільки коли він досягає краю екрану
    elif enemyX >= 735:
        enemyX_change = -4
        enemyY += enemyY_change  # Переміщуємо ворога вниз тільки коли він досягає краю екрану
        # Bullet movement

    if bullet_state is "fire":
            fire_bullet(playerX, bulletY)
            bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    clock.tick(60)
