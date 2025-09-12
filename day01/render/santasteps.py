import pygame
from os.path import join
import pprint

# constants
step_file = join("day01", "render", "step.png")
step_fill_file = join("day01", "render", "step_fill.png")
WINDOW_WIDTH, WINDOW_HEIGHT = 256, 240
SPRITE_WIDTH, SPRITE_HEIGHT = 16, 16
SPEED = 0.009

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Santa vs. Stairs")
running = True

# surfaces
step = pygame.image.load(step_file).convert_alpha()
step_fill = pygame.image.load(step_fill_file).convert()

# calculate all step heights
step_positions = []
start_pos = (int(0), int((WINDOW_HEIGHT/2)-SPRITE_HEIGHT))
curr_pos = start_pos
step_positions.append(curr_pos)

filename = "day01/input.txt"
with open(filename) as opened_file:
    line = opened_file.readline()

floor = 0
for i, char in enumerate(line, 1):
    if char == "(":
        floor += 1
        step_positions.append((step_positions[i-1][0]+SPRITE_WIDTH, step_positions[i-1][1]+SPRITE_HEIGHT))
    elif char == ")":
        floor -= 1
        step_positions.append((step_positions[i-1][0]+SPRITE_WIDTH, step_positions[i-1][1]-SPRITE_HEIGHT))

max_sprites_on_screen = int(WINDOW_WIDTH/SPRITE_WIDTH) + 1
curr_step = 0

# # iterate through 17 steps starting at curr_step
# for i, cstep in enumerate(step_positions[curr_step:curr_step+max_sprites_on_screen], start=curr_step):
#     print(cstep)

# event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game background
    display_surface.fill(pygame.Color(49, 54, 110))

    # draw steps in view
    for i, step_pos in enumerate(step_positions[curr_step:curr_step+max_sprites_on_screen], start=curr_step):
        display_surface.blit(step, (step_pos[0], step_pos[1]))
        next_pos = step_pos
        while next_pos[1] < WINDOW_HEIGHT:
            next_pos = (next_pos[0], next_pos[1]+SPRITE_HEIGHT)
            display_surface.blit(step_fill, (next_pos[0], next_pos[1]))
        step_pos = (step_pos[0]-SPEED, step_pos[1])
    pygame.display.flip()

pygame.quit()