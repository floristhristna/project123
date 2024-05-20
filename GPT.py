import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
# Bkground
background = pygame.image.load('imgonline-com-ua-pixelizationyrGUycBVbnME.jpg')
# Screen
pygame.display.set_caption("Space Villains")
icon = pygame.image.load('001-icon-6685200.png')
pygame.display.set_icon(icon)
# інопрешеленець
playerImg = pygame.image.load('spaceship.png')
playerX = 350
playerY = 480
playerX_change = 0
# Enemy
enemyImg = pygame.image.load('002-ufo.png')
enemyX = random.randint(0, 750)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 30
# Bullet
bulletImg = pygame.image.load('fire.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  #не видно

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"  # Bullet will be visible
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX)**2 + (enemyY - bulletY)**2)**0.5
    if distance < 27:  # перевіряє відстань
        return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # RGB
    screen.fill((10, 10, 100))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # шоб вікно не закривалось і не скакало
            running = False

        # Keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:# якщо більше то він почне рухатись сам по ординаті
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player
    playerX += playerX_change# шоб не вилітав за межі
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    # Enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 735:
        enemyX_change = -4
        enemyY += enemyY_change

    # Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Check for collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480  # Reset the bullet
        bullet_state = "ready"
        enemyX = random.randint(0, 735)  # перекинаю на нову локацію
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    clock.tick(60)
