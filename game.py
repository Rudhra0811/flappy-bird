import pygame, sys, random
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.sprite = pygame.image.load('bird.png')
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), self.sprite.get_height())
        self.velocity = 5

pygame.init()

screen_width = 1280
screen_height = 720
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height)) 

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

player = Player(100, 100)

gravity = 0.5

game_over = False
score = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    # Restart the game
                    player.rect.y = 100
                    player.velocity = 0
                    game_over = False
                    score = 0
                else:
                    player.velocity = -10

    if not game_over:
        player.velocity += gravity

        if player.rect.y + player.rect.height < screen_height:
            player.rect.y += player.velocity

        if player.rect.y + player.rect.height >= screen_height:
            game_over = True

    screen.fill(white)
    screen.blit(background, (0, 0))
    screen.blit(player.sprite, player.rect)

    if game_over:
        # Display "Game Over" in red color
        font = pygame.font.Font(None, 102)
        text = font.render("Game Over!!", True, red)
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(text, text_rect)

        # Display "Press space to restart" in blue color and small size below
        font = pygame.font.Font(None, 24)
        restart_text = font.render("Press space to restart", True, blue)
        restart_text_rect = restart_text.get_rect(center=(screen_width/2, screen_height/2 + 50))
        screen.blit(restart_text, restart_text_rect)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
