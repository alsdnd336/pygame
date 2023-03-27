import pygame
import random
pygame.init()

screen_wdith = 480
screen_height = 640
screen = pygame.display.set_mode((screen_wdith, screen_height))
clock = pygame.time.Clock()
total_time = 30

start_ticks = pygame.time.get_ticks()

pygame.display.set_caption("내 맘대로 게임")

game_font = pygame.font.Font(None, 40)

bg_img = pygame.image.load("D:\\CODING\\pygame\\background.png")

character = pygame.image.load("D:\\CODING\\pygame\\character.png")
character_size = character.get_rect().size
character_wdith = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_wdith / 2) - (character_wdith / 2)
character_y_pos = screen_height - character_height

enemy = pygame.image.load("D:\\CODING\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_wdith - enemy_width)
enemy_y_pos = 0
enemy_speed = 30


# 이동할 죄표
to_x = 0

character_speed = 0.5

runing = True
while runing:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_wdith - character_wdith:
        character_x_pos = screen_wdith - character_wdith
    
    # 충돌 처리를 위한 rect 설정을 
    # rect을 통해 겹치는 부분을 판별하여 충돌 처리를 한다.

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_wdith - enemy_width)

    if character_rect.colliderect(enemy_rect):
        print("충돌했어 이놈아!")
        runing = False



    screen.blit(bg_img,(0, 0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000


    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))
    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()