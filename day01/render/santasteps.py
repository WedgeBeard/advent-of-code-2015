import pygame
import os

# constants
step_file = "day01/render/step.png"

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 256, 240
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Santa vs. Stairs")
running = True

# surface
surf = pygame.Surface((1,1))
step = pygame.image.load(step_file)

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill(pygame.Color(49, 54, 110))
    display_surface.blit(surf, (20,20))
    display_surface.blit(step, (30,30))
    display_surface.blit(step, (46,46))
    pygame.display.flip()


pygame.QUIT()