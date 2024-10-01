import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_WIDTH = 80
TARGET_HEIGHT = 80

# Инициализация окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра <Тир>")

# Установка иконки
icon = pygame.image.load("img/Тир.png")
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_img = pygame.image.load("img/target.png")

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Задание FPS
clock = pygame.time.Clock()


def draw_target(x, y):
    """Функция для отрисовки мишени на экране."""
    screen.blit(target_img, (x, y))


def update_target_position():
    """Функция для обновления позиции мишени."""
    return random.randint(0, SCREEN_WIDTH - TARGET_WIDTH), random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)


def is_target_hit(mouse_x, mouse_y, target_x, target_y):
    """Проверка попадания по мишени."""
    return target_x < mouse_x < target_x + TARGET_WIDTH and target_y < mouse_y < target_y + TARGET_HEIGHT


# Основной игровой цикл
running = True
while running:
    screen.fill(color)  # Закраска экрана случайным цветом
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if is_target_hit(mouse_x, mouse_y, target_x, target_y):
                target_x, target_y = update_target_position()

    draw_target(target_x, target_y)
    pygame.display.update()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
