import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)


sky_surface=pygame.image.load('graphics/Sky.png')
ground_surface=pygame.image.load('graphics/ground.png')
test_surface=test_font.render("Strat the game",False,'Black')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #draw all our elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    #update everything
    pygame.display.update()
    clock.tick(60)