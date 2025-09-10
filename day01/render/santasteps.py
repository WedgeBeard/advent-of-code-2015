import pygame
from os.path import join

# constants
step_file = join("day01", "render", "step.png")
step_fill_file = join("day01", "render", "step_fill.png")

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 256, 240
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Santa vs. Stairs")
running = True

# surface
step = pygame.image.load(step_file).convert_alpha()
step_fill = pygame.image.load(step_fill_file).convert()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game background
    display_surface.fill(pygame.Color(49, 54, 110))

    # first step
    curr_pos = (0, (WINDOW_HEIGHT/2)-16)
    display_surface.blit(step, (curr_pos[0], curr_pos[1]))
    while curr_pos[1] < WINDOW_HEIGHT:
        curr_pos = (curr_pos[0], curr_pos[1]+16)
        display_surface.blit(step_fill, (curr_pos[0], curr_pos[1]))
    pygame.display.flip()

pygame.quit()