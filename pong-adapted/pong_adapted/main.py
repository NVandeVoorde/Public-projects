import pygame

pygame.init()

# Initialize game

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adapted pong game")
run = True 

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK =  (0, 0, 0)

# Ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
ball_vel_x, ball_vel_y = 0.25, 0.25

# Paddle 
paddle_width, paddle_height = 20, 120
left_paddle_y =  right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - 100 - paddle_width/2


# mainloop 

while run: 
    wn.fill(BLACK)
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            run = False
        
    # Wall bounces 
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius: 
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius: 
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 - radius: 
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        ball_vel_x, ball_vel_y = 0.25, 0.25


    # Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
            
    # Elements
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()