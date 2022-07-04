#!/usr/bin/python3

import pygame, sys, os.path

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([800,600])


class Game:
    def __init__(self):
        # create rectangles
        self.player = pygame.Rect(350,560,100,20)
        self.ball = pygame.Rect(400,300,30,30)
        # don't hit this, or you will loose (just avoid it)!
        self.avoid = pygame.Rect(380,80,20,20)

        self.score = 0
        self.lifes = 3
        # ball speed
        self.speed_x, self.speed_y = 5,5
        # font
        self.font = pygame.font.Font("FONT.ttf",40)

    def player_movement(self):
        # move the player on axis by pressing right and left arrow keys
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.x += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.x -= 5

    def ball_movement(self):
        # move ball
        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y
        # bounce when collide with borders
        if self.ball.x >= 770 or self.ball.x <= 0:
            self.speed_x*=-1
        if self.ball.y >= 570 or self.ball.y <= 0:
            self.speed_y*=-1
        # bounce when collide with player
        if pygame.Rect.colliderect(self.player, self.ball):
            self.speed_y*=-1
            # update score
            self.score += 1

    def looserect_movement(self):
        # move red rectangle
        avoid_x, avoid_y = 3,3
        self.avoid.x += avoid_x
        self.avoid.y += avoid_y
        # bounce when collide with borders
        if self.avoid.x >= 780 or self.avoid.x <= 0:
            avoid_x*=-1
        if self.avoid.y >= 580 or self.avoid.y <= 0:
            avoid_y*=-1
        # loose when collides with player
        if pygame.Rect.colliderect(self.player, self.avoid):
            self.lifes = 0

    def draw(self, surface):
        # draw the rects
        pygame.draw.rect(surface, (255,255,255), self.player)
        pygame.draw.rect(surface, (255,255,255), self.ball)
        pygame.draw.rect(surface, (255,0,0), self.avoid)
        # draw score and lifes
        score_msg = self.font.render("Score  " + str(self.score), False, (255,255,255))
        lifes_msg = self.font.render("Lifes  " + str(self.lifes), False, (255,255,255))
        surface.blit(score_msg, (20,20))
        surface.blit(lifes_msg, (630,20))

    def game_utility(self, surface):
        # subtract 1 to lifes and loose whent it's = 0
        if self.ball.y >= 570:
            self.lifes -= 1
        if self.lifes == 0:
            sys.exit()
        # report the score in a file
        if os.path.exists(".scores.txt"):
            print("exist")
            with open(".scores.txt","a") as f:
                f.write(str(self.score)+"\n")
        else:
            print("don't exist")
            os.system("touch .scores.txt")

game = Game()

def call_func(ob):
    ob.player_movement()
    ob.ball_movement()
    ob.looserect_movement()
    ob.draw(screen)
    ob.game_utility(screen)

# --- MAIN LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    # --- BODY ---
    call_func(game)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
