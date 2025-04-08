import pygame
import time

pygame.init()

WIDTH, HEIGHT = 600, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
transColor = (255, 255, 255) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("mickey_face.jpeg").convert()
minute_hand = pygame.image.load("leftarm.png").convert()
second_hand = pygame.image.load("rightarm.png").convert()

minute_hand.set_colorkey(transColor)
second_hand.set_colorkey(transColor)

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (250, 80))
second_hand = pygame.transform.scale(second_hand, (250, 80))

# Функция поворота и отрисовки стрелок
def draw_rotated(image, angle, position):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=position)
    screen.blit(rotated_image, new_rect.topleft)

# Основной цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0, 0))

    # Получаем текущее время
    c = time.localtime()
    minutes = c.tm_min
    seconds = c.tm_sec

    # Вычисляем углы поворота
    minute_angle = - (minutes * 6)
    second_angle = - (seconds * 6) 

    # Рисуем стрелки
    draw_rotated(minute_hand, minute_angle, CENTER)
    draw_rotated(second_hand, second_angle, CENTER)

    pygame.display.update()
    
    # Ограничиваем FPS
    clock.tick(60)

    # Проверяем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
