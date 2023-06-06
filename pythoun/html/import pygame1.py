import pygame
import random
import time

# 게임 화면 크기
WIDTH, HEIGHT = 800, 600

# 색상 정의
WHITE = (255, 255, 255)

# 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1인용 핑퐁 게임")

clock = pygame.time.Clock()

# 패들 설정
paddle_width = 80
paddle_height = 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 50
paddle_speed = 5

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 3
ball_dy = -3
ball_speed_increase = 0.1

# 게임 정보
score = 0
chances = 3
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
game_over = False
game_over_time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # 패들 이동 범위 제한
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > WIDTH - paddle_width:
        paddle_x = WIDTH - paddle_width

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 경계 체크
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius:
        ball_dx *= -1

    # 바닥에 닿으면 게임 기회 감소
    if ball_y >= HEIGHT - ball_radius:
        chances -= 1
        if chances <= 0:
            game_over = True
            game_over_time = time.time()

        # 게임 기회가 남아있을 때 공 초기화
        else:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dx = 3
            ball_dy = -3

    # 패들과의 충돌 체크
    if paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy *= -1
        score += 100
        ball_dx += random.uniform(-ball_speed_increase, ball_speed_increase)
        ball_dy += random.uniform(-ball_speed_increase, ball_speed_increase)

        # 패들에 닿을 때마다 공의 속도 증가
        ball_dx *= 1.05
        ball_dy *= 1.05

    # 천장에 닿으면 공 튕김
if ball_y <= ball_radius:
        ball_dy *= -1

    # 화면 업데이트
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # 점수 및 게임 기회 표시
    score_text = font.render("Score: {}".format(score), True, WHITE)
    chances_text = font.render("Chances: {}".format(chances), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(chances_text, (WIDTH - chances_text.get_width() - 10, 10))

    # 게임 종료 표시
    if game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        # 게임 종료 후 3초 대기
        if time.time() - game_over_time >= 3:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()