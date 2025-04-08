import pygame
import sys
import random as ran
import classGame  
pygame.init()
pygame.mixer.init()
# Music MARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!
monetka = pygame.mixer.Sound("z_uki-dlya-_ideo-z_uk-monetok-mario.mp3")

# Константы       
WIDTH, HEIGHT = 1500, 800
BLACK = (0, 0, 0)
CELL_SIZE = 20
INTERVAL = 2000

# Обычная переменая
tick_speed = 13
level_up = True
play_game = True
food = False
monetka_music = False
time_set = 0
special_food = False
# Разные методы из пайгем
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Snake')
start_time = pygame.time.get_ticks()

# Цвет тело и головы
GREEN = (0, 255, 0)
WHITE = (255,255,255)

# Массивы игры
obstacles = []
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
# Направление
direction = 'RIGHT'
change_to = direction
        
ui = classGame.UI_Count(WIDTH - 100, 20, 80, 40, (50, 50, 50), 36)
clock = pygame.time.Clock()


running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        # Выход из игры
        if event.type == pygame.QUIT:
            running = False
        # Методы изменения направления 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_s and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_d and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_a and direction != 'RIGHT':
                change_to = 'LEFT'
        elif event.type == pygame.MOUSEBUTTONUP:
            if play_game == False: 
                pos = event.pos
                if button_exit.rect.collidepoint(pos):
                    running = False
                if button_replay.rect.collidepoint(pos):
                    tick_speed = 13
                    level_up = True
                    play_game = True
                    food = False
                    # Массивы игры
                    obstacles = []
                    snake_pos = [100, 100]
                    snake_body = [[100, 100], [80, 100], [60, 100]]
                    # Направление
                    direction = 'RIGHT'
                    change_to = direction
                            
                    ui = classGame.UI_Count(WIDTH - 100, 20, 80, 40, (50, 50, 50), 36)

                    
    for i in range(1, len(snake_body)):
        if snake_body[0][0] == snake_body[i][0] and snake_body[0][1] == snake_body[i][1]:
            play_game = False
            pygame.mixer.music.load("mario-smert.mp3")
            pygame.mixer.music.play()


    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load("super-mario-saundtrek.mp3")
        pygame.mixer.music.play()
    direction = change_to
    
    # Создание еды по интервалу 
    if current_time - start_time >= INTERVAL:
        if food == False: 
            food_x = ran.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            food_y = ran.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            choose = ran.randint(1,3)
            if choose == 1:
                food = classGame.GameObject(food_x, food_y, CELL_SIZE, CELL_SIZE, (255, 255, 255),1)
            elif choose == 2:
                food = classGame.GameObject(food_x, food_y, CELL_SIZE, CELL_SIZE, (255, 255, 255),2)
            elif choose == 3: 
                food = classGame.GameObject(food_x, food_y, CELL_SIZE , CELL_SIZE, (255,0,0),3)
                line_time = pygame.Rect(700, 30,300,10 )
                special_food = True
            obstacles.append(food)
            food = True
    if current_time - start_time >= INTERVAL:
        time_set += 1
    # Проверка столкновения с едой.
    player = pygame.Rect(snake_pos[0], snake_pos[1], CELL_SIZE, CELL_SIZE)
    for obstacle in obstacles[:]:
        if player.colliderect(obstacle.rect):
            obj : classGame.GameObject = obstacle
            ui.count_more(obj.get_weight()) 
            obstacles.remove(obstacle)
            snake_body.insert(0, list(snake_pos))
            special_food = False
            line_time = None
            level_up =True
            monetka.play()
            monetka_music = True
            food =False
            
            


    # Отрубить монетку
    if time_set % 10 == 0:
        monetka_music = False
    if monetka_music == False:
        monetka.stop()
    
    #     
    if special_food:
        line_time.width -= 5
        if line_time.width == 0: 
            obstacles.clear()
            special_food = False
            line_time = None
            food =False

    
    # Проверка уровня и увелечение его скорости 
    if ui.num % 5 == 0 and ui.num != 0 and level_up: 
        level_up = False
        tick_speed += 0.5
            
    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE 
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE 
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE 
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE 

    if snake_pos[0] < 0:
        snake_pos[0] = WIDTH - CELL_SIZE 
    elif snake_pos[0] >= WIDTH:
        snake_pos[0] = 0 
    elif snake_pos[1] < 0:
        snake_pos[1] = HEIGHT - CELL_SIZE 
    elif snake_pos[1] >= HEIGHT:
        snake_pos[1] = 0
    
    snake_body.insert(0, list(snake_pos))
    snake_body.pop()

    screen.fill(BLACK)
    # Обработка данных
    if play_game == True: 
        for i in range(1,len(snake_body)):
            pygame.draw.rect(screen, GREEN, pygame.Rect(snake_body[i][0], snake_body[i][1], CELL_SIZE, CELL_SIZE))
        for obstacle in obstacles: 
            obstacle.draw(screen)    
            
        pygame.draw.rect(screen, WHITE, pygame.Rect(snake_pos[0], snake_pos[1], CELL_SIZE, CELL_SIZE))
        if(special_food):
            pygame.draw.rect(screen, (255,255,255), line_time)
        ui.draw(screen)
    else: 
        game_over = classGame.UI_level(0,0,WIDTH, HEIGHT, (200,0,0),80, "Game Over!" )
        button_replay = classGame.Button(580, 450,150,60, (0,0,0), "Replay", (255,255,255), 5)
        button_exit = classGame.Button(780, 450,150,60, (0,0,0), "Exit", (255,255,255), 5)        
        game_over.draw(screen)
        button_exit.draw(screen)
        button_replay.draw(screen)
    pygame.display.flip()
    clock.tick(tick_speed)

pygame.quit()
sys.exit()

