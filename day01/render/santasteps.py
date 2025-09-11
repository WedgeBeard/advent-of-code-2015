import pygame
from os.path import join
import pprint

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

steps_on_screen = []
start_pos = (0, (WINDOW_HEIGHT/2)-16)
curr_pos = start_pos
steps_on_screen.append(curr_pos)

filename = "day01/input.txt"
with open(filename) as opened_file:
    line = opened_file.readline()

print(len(line))
floor = 0
for i, char in enumerate(line, 1):
    if char == "(":
        floor += 1
        steps_on_screen.append((steps_on_screen[i-1][0]+16, steps_on_screen[i-1][1]+16))
    elif char == ")":
        floor -= 1
        steps_on_screen.append((steps_on_screen[i-1][0]+16, steps_on_screen[i-1][1]-16))
    

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