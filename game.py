import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)


sky_surface=pygame.image.load('graphics/Sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()
test_surface=test_font.render("Strat the game",False,'Black')

snail_surf=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect=snail_surf.get_rect(bottomright=(600,300))

player_surf=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #draw all our elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))

    if snail_rect.right <= 0 :snail_rect.left=800
    snail_rect.x -=4

    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    #update everything
    pygame.display.update()
    clock.tick(60)