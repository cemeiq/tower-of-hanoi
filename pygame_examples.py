import pygame

over = False
# pygame globals
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tower of Hanoi')
background = pygame.image.load("/home/iqra/Tower_of_hanoi/background.jpeg")
black = (0, 0, 0)
running = True

while running:
    screen.fill((230, 230, 230))    
    # to add the background after the solid white fill
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (255,0,0) ,pygame.R)
