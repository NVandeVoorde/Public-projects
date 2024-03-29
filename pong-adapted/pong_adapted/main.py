import pygame
import random
import time

pygame.init()

# Initialize game

WIDTH, HEIGHT = 1200, 800
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adapted pong game")
run = True 
direction = [0, 1]
angle = [0, 1, 2]
left_points = 0
right_points = 0 


# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)



# Ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
ball_vel_x, ball_vel_y = 0.25, 0.25

# Paddle 
paddle_width, paddle_height = 20, 100
left_paddle_y =  right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - paddle_width / 2, WIDTH - 100 - paddle_width / 2
right_paddle_vel = left_paddle_vel = 0 

# Gadgets
left_gadget = right_gadget = 0 
left_gadget_remaining = right_gadget_remaining = 5



# Mainloop 

while run: 
    wn.fill(BLACK)

    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            run = False
        # Pressing keys
        elif i.type == pygame.KEYDOWN: 
            if i.key == pygame.K_UP: 
                right_paddle_vel = -1
            if i.key == pygame.K_DOWN: 
                right_paddle_vel = 1
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0: 
                right_gadget = 1
            if i.key == pygame.K_w: 
                left_paddle_vel = -1
            if i.key == pygame.K_s: 
                left_paddle_vel = 1
            if i.key == pygame.K_d and left_gadget_remaining > 0: 
                left_gadget = 1
        # Key release
        if i.type == pygame.KEYUP: 
            right_paddle_vel = 0
            left_paddle_vel = 0
        
    # Wall bounces 
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius: 
        ball_vel_y *= -1
        # ball outside on right
    if ball_x >= WIDTH - radius:        
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        left_points += 1
        pygame.time.wait(1000)
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0: 
            if ang == 0: 
                ball_vel_y, ball_vel_x = -0.35, 0.25
            if ang == 1: 
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2: 
                ball_vel_y, ball_vel_x = -0.25, 0.35
        if dir == 1: 
            if ang == 0: 
                ball_vel_y, ball_vel_x = 0.35, 0.25
            if ang == 1: 
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2: 
                ball_vel_y, ball_vel_x = 0.25, 0.35
        ball_vel_x *= -1
        # ball outside on left 
    if ball_x <= 0 - radius: 
        right_points += 1
        pygame.time.wait(1000)
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        ball_vel_x, ball_vel_y = 0.25, 0.25
        if dir == 0: 
            if ang == 0: 
                ball_vel_y, ball_vel_x = -0.35, 0.25
            if ang == 1: 
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2: 
                ball_vel_y, ball_vel_x = -0.25, 0.35
        if dir == 1: 
            if ang == 0: 
                ball_vel_y, ball_vel_x = 0.35, 0.25
            if ang == 1: 
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2: 
                ball_vel_y, ball_vel_x = 0.25, 0.35

    # Paddle collisions
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height: 
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height: 
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # Gadget smash 
    if left_gadget == 1: 
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height: 
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -2.5
                left_gadget = 0 
                left_gadget_remaining -= 1
    
    if right_gadget == 1: 
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height: 
                ball_x = right_paddle_x
                ball_vel_x *= -2.5
                right_gadget = 0 
                right_gadget_remaining -= 1

    # Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel

    # Paddle movement 
    if right_paddle_y >= HEIGHT - paddle_height: 
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0: 
        right_paddle_y = 0
    if left_paddle_y >= HEIGHT - paddle_height: 
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0: 
        left_paddle_y = 0


            
    # Elements
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    
    # Text
    font1 = pygame.font.SysFont('Arial', 24)
    text1 = font1.render(str(left_points) + " - " + str(right_points), True, WHITE)
    textRect1 = text1.get_rect()
    textRect1.center = (WIDTH/2, 0 + 20)
    wn.blit(text1, textRect1)
    
    pygame.display.update()