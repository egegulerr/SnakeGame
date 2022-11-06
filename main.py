import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

width, height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ege's Snake Game!")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)


def draw_score(score):
    score_text = score_font.render(f"Score: {score}", True, ORANGE)
    window.blit(score_text, [0, 0])


def draw_snake(snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, WHITE, [pixel[0], pixel[1], snake_size, snake_size])


def draw_message(message):
    text = message_font.render(message, True, RED)
    window.blit(text, [width / 2 - 250, height / 2])


def get_target_positions():
    x_target = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    y_target = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    return x_target, y_target


def run_game():
    game_over = False
    game_close = False

    x_position, y_position = width / 2, height / 2
    x_new_pos, y_new_pos = 0, 0

    snake_pixels = []
    snake_length = 1
    x_target, y_target = get_target_positions()
    while not game_close:
        while game_over:
            window.fill(BLACK)
            draw_message("GAME OVER! Press Any Key To Play Again")
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_new_pos = -snake_size
                    y_new_pos = 0
                if event.key == pygame.K_RIGHT:
                    x_new_pos = snake_size
                    y_new_pos = 0
                if event.key == pygame.K_UP:
                    x_new_pos = 0
                    y_new_pos = -snake_size
                if event.key == pygame.K_DOWN:
                    x_new_pos = 0
                    y_new_pos = snake_size

        if (
            x_position <= 0
            or x_position > width
            or y_position <= 0
            or y_position > height
        ):
            game_over = True

        x_position += x_new_pos
        y_position += y_new_pos

        window.fill(BLACK)
        pygame.draw.rect(window, ORANGE, [x_target, y_target, snake_size, snake_size])

        snake_pixels.append([x_position, y_position])
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[1:-1]:
            if pixel == [x_position, y_position]:
                game_over = True

        draw_snake(snake_pixels)
        draw_score(snake_length - 1)
        pygame.display.update()

        if x_position == x_target and y_position == y_target:
            x_target, y_target = get_target_positions()
            snake_length += 1

        clock.tick(snake_speed)  # TODO What happen when 100 ?

    pygame.quit()
    quit()

run_game()
