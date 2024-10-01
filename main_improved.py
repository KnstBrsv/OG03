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

# Загрузка звука попадания
hit_sound = pygame.mixer.Sound("sounds/hit.wav")

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

# Скорость мишени
target_speed_x = random.choice([-3, 3])
target_speed_y = random.choice([-3, 3])

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт для подсчета очков
font = pygame.font.Font(None, 36)

# Начальные очки
score = 0

# Задание FPS
clock = pygame.time.Clock()


def draw_target(x, y):
    """Функция для отрисовки мишени на экране."""
    screen.blit(target_img, (x, y))


def update_target_position(x, y, speed_x, speed_y):
    """Функция для обновления позиции мишени с учётом границ экрана."""
    x += speed_x
    y += speed_y

    # Проверка выхода за границы экрана и изменение направления
    if x <= 0 or x >= SCREEN_WIDTH - TARGET_WIDTH:
        speed_x = -speed_x
    if y <= 0 or y >= SCREEN_HEIGHT - TARGET_HEIGHT:
        speed_y = -speed_y

    return x, y, speed_x, speed_y


def is_target_hit(mouse_x, mouse_y, target_x, target_y):
    """Проверка попадания по мишени."""
    return target_x < mouse_x < target_x + TARGET_WIDTH and target_y < mouse_y < target_y + TARGET_HEIGHT


def draw_score(score):
    """Функция для отображения текущего счёта."""
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


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
                # Обновление счёта и перемещение мишени
                score += 1
                target_x, target_y = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH), random.randint(0,
                                                                                                    SCREEN_HEIGHT - TARGET_HEIGHT)
                hit_sound.play()  # Проигрывание звука попадания

    # Обновление позиции мишени
    target_x, target_y, target_speed_x, target_speed_y = update_target_position(target_x, target_y, target_speed_x,
                                                                                target_speed_y)

    # Отрисовка мишени и счёта
    draw_target(target_x, target_y)
    draw_score(score)

    pygame.display.update()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
