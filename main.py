# game   window
import  pygame
import random

#initializing pygame
pygame.init()

#background
background = pygame.image.load('space_.png')


# create the screen
screen = pygame.display.set_mode((800, 600))

# game title and Icon
pygame.display.set_caption(" Space invaders ")

icon = pygame.image.load("ufo-2.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load("player2.png")
player_X = 370
player_y = 480

player_X_change = 0

#enemy
enemy_img = pygame.image.load("enemy.png")
enemy_X = random.randint(0, 800)
enemy_y = random.randint(50, 150)

enemy_X_change = 0.3
enemy_y_change = 40


# positioning the player
def player(x, y):
     screen.blit(player_img, (x, y))


# positioning the player
def enemy(x, y):
     screen.blit(enemy_img, (x, y))


# game loop
running = True
while running:
     #RGB 
     screen.fill((0, 0, 0))
      #background image
     screen.blit(background, (0, 0))    
    
     for event in pygame.event.get ():
          if event.type == pygame.QUIT:
               running = False

   #if keystroke is pressed check whether it is right or left
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    player_X_change = -0.3
                    # print("left arrow key is pressed")

          if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_RIGHT:
                               player_X_change = 0.3
                              # print("right arrow key is pressed")
           
           
          if event.type == pygame.KEYUP:
                         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                               player_X_change = 0
                              # print("Key stroke has been released ")



     player_X += player_X_change
     enemy_X += enemy_X_change

# checking for boundaries of spaceship so that it does not go out of bound
     if player_X <= 0:
          player_X = 0
     elif player_X >= 750:    
          player_X = 750

     if enemy_X <= 0:
          enemy_X_change = 0.3
          enemy_y += enemy_y_change

     elif enemy_X >= 750:    
          enemy_X_change = -0.3
          enemy_y += enemy_y_change

     player(player_X, player_y)
     enemy(enemy_X, enemy_y)
     pygame.display.update()