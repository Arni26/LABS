import pygame

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Paint")
CLOCK = pygame.time.Clock()

# Холст
canvas = pygame.Surface(screen.get_size())
canvas.fill((255, 255, 255))

# Загрузка значков инструментов
image_rectangle = pygame.image.load("rectangle.png")
image_circle = pygame.image.load("circle.png")

# Список цветов
colors = [
    {"name": "white", "image": pygame.image.load("whit.png"), "color": (255, 255, 255)},
    {"name": "black", "image": pygame.image.load("blac.png"), "color": (0, 0, 0)},
    {"name": "darkRed", "image": pygame.image.load("darkRed.png"), "color": (139, 0, 0)},
    {"name": "gray", "image": pygame.image.load("gray.png"), "color": (128, 128, 128)},
    {"name": "grayLight", "image": pygame.image.load("grayLight.png"), "color": (169, 169, 169)},
    {"name": "lightOrange", "image": pygame.image.load("lightOrange.png"), "color": (255, 140, 0)}
]

# Установка позиций кнопок инструментов
rectangle_rect = image_rectangle.get_rect(topleft=(10, 10))
circle_rect = image_circle.get_rect(topleft=(rectangle_rect.right + 10, 10))

# Установка позиций кнопок цветов
x_offset = 900  # Начальная позиция для цветов
for color in colors:
    color["rect"] = color["image"].get_rect(topleft=(x_offset, 10))
    x_offset += color["rect"].width + 10

# Переменные
running = True
color_brush = (0, 0, 0)
brush_size = 10
prev_pos = None  
current_tool = "brush"
drawing = False  
start_pos = None  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия на инструменты
            if rectangle_rect.collidepoint(pos):
                current_tool = "rectangle"
            elif circle_rect.collidepoint(pos):
                current_tool = "circle"

            # Если выбрана фигура, начинаем рисование
            elif current_tool in ["rectangle", "circle"]:
                start_pos = pos
                drawing = True
            # Проверка нажатия на цвета
            for color in colors:
                if color["rect"].collidepoint(pos):
                    color_brush = color["color"]

        # Рисование кистью и ластиком
        if pygame.mouse.get_pressed()[0] and current_tool in ["brush", "eraser"]:
            color = (255, 255, 255) if current_tool == "eraser" else color_brush
            if prev_pos is not None:
                pygame.draw.line(canvas, color, prev_pos, pos, brush_size * 2)
            prev_pos = pos
        else:
            prev_pos = None

        # Отпускание кнопки мыши - рисование фигур
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            top_left = (min(x1, x2), min(y1, y2))

            if current_tool == "rectangle":
                pygame.draw.rect(canvas, color_brush, (*top_left, width, height), 2)
            elif current_tool == "circle":
                radius = max(width, height) // 2
                center = (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
                pygame.draw.circle(canvas, color_brush, center, radius, 2)

            drawing = False
            start_pos = None
        
        # Горячие клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                current_tool = "brush"
            elif event.key == pygame.K_e:
                current_tool = "eraser"

    # Отрисовка холста и кнопок
    screen.blit(canvas, (0, 0))
    screen.blit(image_rectangle, rectangle_rect)
    screen.blit(image_circle, circle_rect)
    for color in colors:
        screen.blit(color["image"], color["rect"])

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
