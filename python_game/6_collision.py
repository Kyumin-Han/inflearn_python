import pygame

pygame.init() # 초기화 (반드시 필요함)

# 화면 크기 설정
screen_width = 480 # 프레임의 가로 크기
screen_height = 640 # 프레임의 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("First Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\4rbal\\Desktop\\inflearn\\python\\python_game\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\4rbal\\Desktop\\inflearn\\python\\python_game\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해온다
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 x위치로 지정
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 y위치로 지정

# 이동 할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\4rbal\\Desktop\\inflearn\\python\\python_game\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해온다
enemy_width = enemy_size[0] # 캐릭터의 가로크기
enemy_height = enemy_size[1] # 캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 x위치로 지정
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 y위치로 지정

# 이벤트 루프
running = True # 게임이 진행중인지 확인하는 변수

while running:
    dt = clock.tick(120) # 게임 화면의 초당 프레임 수를 지정
    # 캐릭터가 1초에 100 만큼 이동 해야 함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동해야함
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동해야함
    # 프레임 별로 이동 시켜야 할 수치가 다르다

    for event in pygame.event.get(): # 파이게임을 사용하기 위해서 무조건 적어주어야 하는 코드(어떤 이벤트가 발생하였는가?)
        if event.type == pygame.QUIT: # 창 닫기 버튼을 눌렀을때 QUIT라는 이벤트가 발생한다
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 프레임에 따른 이동속도를 보정시켜 줄 수 있도록 dt 값을 곱해준다
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 화면을 다시 그리기(실행 되는 도중 계속 실행되야함)

# pygame 종료
pygame.quit()