import pygame

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정
screen_width = 480 # 프레임의 가로 크기
screen_height = 640 # 프레임의 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("First Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\4rbal\\Desktop\\inflearn\\python\\python_game\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\4rbal\\Desktop\\inflearn\\python\\python_game\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해온다
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 x위치로 지정
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 y위치로 지정


# 이벤트 루프
running = True # 게임이 진행중인지 확인하는 변수

while running:
    for event in pygame.event.get(): # 파이게임을 사용하기 위해서 무조건 적어주어야 하는 코드(어떤 이벤트가 발생하였는가?)
        if event.type == pygame.QUIT: # 창 닫기 버튼을 눌렀을때 QUIT라는 이벤트가 발생한다
            running = False
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 화면을 다시 그리기(실행 되는 도중 계속 실행되야함)

# pygame 종료
pygame.quit()