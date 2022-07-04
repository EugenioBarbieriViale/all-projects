#!/usr/bin/python3

import pygame, random, time

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode([800,600])
pygame.display.set_caption("Arcade - by Eugenio")

score_font = pygame.font.Font("score_font.ttf", 40)
loose_font = pygame.font.Font("score_font.ttf", 80)
play_again_font = pygame.font.Font("score_font.ttf", 55)

score = 0
lifes = 3
# gravity
g = 2
# create rects
player = pygame.Rect(350,560,100,20)
catch = pygame.Rect(400,40,30,30)
play_again = pygame.Rect(277,260,200,70)
quit = pygame.Rect(295,350,160,60)

def move_player():
    global player
    # move player by pressing right and left arrows keys
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.x += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.x -= 5
    # draw player
    player_draw = pygame.draw.rect(window, (255,255,255), player)

def fall_rects():
    global player, catch, g, score, score_font
    catch.y += g
    # if the falling rect collides with player, reset y position and generete a new random x position
    if pygame.Rect.colliderect(catch, player):
        catch.x = random.randint(30,770)
        catch.y = 40
        score += 1
        # increase falling speed of rects until g=5
        if g<=5:
            g += 0.2
        else:
            g = 5
    # draw rect
    catch_draw = pygame.draw.rect(window, (255,0,255), catch)
    # display score
    score_msg = score_font.render("Score  " + str(score), False, (255,255,255))
    window.blit(score_msg, (20,20))

def play_case():
    global play_again, window
        if pygame.mouse.get_pressed()[0] and play_again.collidepoint(pygame.mouse.get_pos()):
        window.fill((0,0,0))

def quit_case():
    global quit, run
        if pygame.mouse.get_pressed()[0] and quit.collidepoint(pygame.mouse.get_pos()):
        run = False

def loose():
    global catch, run, window, loose_font, play_again_font, play_again, quit, score_font
    if catch.y >= 620:
        # game over surface
        window.fill((0,0,0))
        loosemsg = loose_font.render("YOU   LOST", True, (255,255,255))
        window.blit(loosemsg, (220,170))
        # play again
        play_again_draw = pygame.draw.rect(window,(255,255,255), play_again, 3)
        play_again_msg = play_again_font.render("PLAY", True, (255,255,255))
        window.blit(play_again_msg, (320,270))
        # quit
        quit_draw = pygame.draw.rect(window, (255,255,255), quit, 3)
        quit_msg = score_font.render("QUIT", True, (255,255,255))
        window.blit(quit_msg, (332,360))
        # play again or quit?
        play_case()
        quit_case()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    window.fill((0,0,0))

    fall_rects()
    move_player()
    loose()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
