import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen =pygame.display.set_mode((screen_width,screen_height))
 

#화면 타이틀 설정
pygame.display.set_caption("Min Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("D:\\CODING\\pygame\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False # 게임이 진행 중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    # screen.fill((0, 0, 255))  # 그냥 배경을 파란 색으로 색칠하는 방법

    # pygame은 프레임마다 배경을 그려줘야 한다.
    pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()   