import pygame
from sys import exit
from random import randint

def display_score():
    currentTime=int(pygame.time.get_ticks()/1000) - start_time
    score_surf =text_font.render(f'Score: {currentTime}', False, (64,64,64))
    score_rect= score_surf.get_rect(center=(400,50))
    screen.blit(score_surf, score_rect)
    return currentTime


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

            
        obstacle_list =[obstacle for obstacle in obstacle_list if obstacle.x >-100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
         for obstacle_rect in obstacles:
             if player.colliderect(obstacle_rect):
                 return False
    return True

def player_animations():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf=player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf=player_walk[int(player_index)]
    return

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock=pygame.time.Clock()
text_font=pygame.font.Font('font/Pixeltype.ttf',50)
game_active=False
start_time=0
score=0

sky_surface=pygame.image.load('graphics/Sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()

# score_surf=text_font.render("My game",False,(64,64,64))
# score_rect=score_surf.get_rect(center=(400,50))


# Enemy obstacles
snail_frame_1=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2=pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames =[snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surf=snail_frames[snail_frame_index]
# snail_rect=snail_surf.get_rect(bottomright=(600,300))

fly_frame_1=pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2=pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames=[fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surf=fly_frames[fly_frame_index]


# fly_rect=fly_surf.get_rect(bottomright=(600,210))

obstacle_rect_list=[]

player_walk_1=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2=pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_jump=pygame.image.load('graphics/player/jump.png').convert_alpha()
player_walk=[player_walk_1, player_walk_2]
player_index=0
player_surf=player_walk[player_index]
player_rect=player_surf.get_rect(midbottom=(80,300))
player_gravity=0

player_stand =pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400, 200))

game_title=text_font.render('The Runner',False, (111,196,169))
game_title_rect=game_title.get_rect(center=(400,80))

game_instruction=text_font.render('Press space to run',False, (111,196,169))
game_instruction_rect=game_instruction.get_rect(center=(400,320))


obstacle_timer=pygame.USEREVENT +1
snail_animation_timer=pygame.USEREVENT +2
fly_animation_timer=pygame.USEREVENT +3
pygame.time.set_timer(obstacle_timer,1500)
pygame.time.set_timer(snail_animation_timer,500)
pygame.time.set_timer(fly_animation_timer,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=300:
                    player_gravity =-20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity =-20
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900,1100),210)))
            if event.type == snail_animation_timer:
                if snail_frame_index==0 :snail_frame_index=1
                else: snail_frame_index=0
                snail_surf=snail_frames[snail_frame_index]
            if event.type ==fly_animation_timer:
                if fly_frame_index==0 :fly_frame_index=1
                else: fly_frame_index=0
                fly_surf=fly_frames[fly_frame_index]

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True
                # snail_rect.left=800
                start_time=int(pygame.time.get_ticks()/1000)

    #draw all our elements
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        # screen.blit(score_surf,score_rect)
        score=display_score()

        # if snail_rect.right <= 0 :snail_rect.left=800
        # snail_rect.x -=4
        # screen.blit(snail_surf,snail_rect)

        #player
        player_gravity+=1
        player_rect.y +=player_gravity
        if player_rect.bottom >=300: player_rect.bottom=300
        player_animations()
        screen.blit(player_surf,player_rect)

        #obstacle move
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)

        #collison
        game_active=collisions(player_rect, obstacle_rect_list)
        # if snail_rect.colliderect(player_rect):
        #     game_active=False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom =(80, 300)
        player_gravity=0
        score_message=text_font.render(f'Your score: {score}',False,(111,196, 169))
        score_message_rect=score_message.get_rect(center=(400, 330))

        
        screen.blit(game_title,game_title_rect)
        if score == 0:
            screen.blit(game_instruction,game_instruction_rect)
        else:
            screen.blit(score_message,score_message_rect)
    # if player_rect.colliderect(snail_rect):
    #     print('collided')

    # mouse_pos=pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())
    # pygame.draw.line(screen, 'Gold',(0,0),pygame.mouse.get_pos(),10)
    # pygame.draw.ellipse(screen,'Brown',pygame.Rect(60,100,100,100))
    # keys=pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]: print("Jump")


    #update everything
    pygame.display.update()
    clock.tick(60)