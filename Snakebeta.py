# import the moubles
import pygame
import random
import time
import datetime
import pickle
import os
import sys
Setter = input("Select hardness,(1)Hard, (2)Normal, (3)Easy ")
Name = input("Please type in your in game name ")
# pygame acts
pygame.init()
# make varibles
Window_width = 700
Window_height = 700
Window = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption("Snake (Beta version)")
today = datetime.datetime.now()
count = 0
width = 40
timer_count = 0
x_leaf = random.randint(0, 660)
y_leaf = random.randint(0, 660)
x = 0
y = 0
Speed = 40
x_mouse = 5
score_plus = 20
y_mouse = 5
lives = 4
Speed_snake = 15
y_button = 630
x_button = 630
leaf_width = 20
font = pygame.font.Font(None, 30)
NameTag_font = pygame.font.Font(None, 15)
Button_font = pygame.font.Font(None, 50)
game_font_over = pygame.font.Font(None, 60)
leaf_height = 20
livegettext = pygame.font.Font(None, 60)
Score_saver = "ScoreSaver.txt"
score = 0
ob1x = x_leaf+120
ob1y = y_leaf+100
f = open("Higs.txt", "a")
x_c = 0
red = pygame.Color(255, 51, 0)
y_c = 0
checkout_y = 640
checkout_x = 580
height = 40
enemies = []
x_gro = 0
y_gro = 640
width_gro = 970
height_gro = 40
running = True
clock = pygame.time.Clock()
# Set up the game loop
while running:
    mouse = pygame.mouse.get_pos()
    (x_mouse, y_mouse) = pygame.mouse.get_pos()
    timer_count = timer_count + 1
    white = pygame.Color(225, 225, 225)
    Window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if Button.colliderect(mousegh):
            running = False
            print("Your score is: " + str(score))
        if mousegh.colliderect(Live):
            lives = lives + 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_c = x_c + -Speed
        y_c = 0
    if keys[pygame.K_RIGHT]:
        x_c = x_c + Speed
        y_c = 0
    if keys[pygame.K_DOWN]:
        y_c = y_c + Speed
        x_c = 0
    if keys[pygame.K_UP]:
        y_c = y_c + -Speed
        x_c = 0
    if keys[pygame.K_h]:
        Speed_snake = Speed_snake - 2
        print("You used a cheat code!")
    if keys[pygame.K_s]:
        print("You used a cheat code!")
        Speed_snake = Speed_snake + 2
    x = x + x_c
    y = y + y_c
    clock.tick(Speed_snake)
    char1 = pygame.draw.rect(Window, (255, 51, 0), (x_leaf, y_leaf, leaf_width, leaf_height))
    Live = pygame.draw.rect(Window, (0, 0, 0), (x_button, y_button-60, 100, 35))
    mousegh = pygame.draw.rect(Window, (0, 0, 0), (x_mouse, y_mouse, 15, 15))
    ob1 = pygame.draw.rect(Window, (0, 0, 0), (ob1x, ob1y, leaf_width, leaf_height))
    Button = pygame.draw.rect(Window, (0, 0, 0), (x_button, y_button, 100, 35))
    checkout = pygame.draw.rect(Window, red, (checkout_x, checkout_y, 15, 15))
    Button_say = Button_font.render("Exit", True, red)
    Window.blit(Button_say, (x_button, y_button + 2))
    char = pygame.draw.rect(Window, (0, 204, 102), (x, y, width, height))
    for Time in range(0, 1000):
        count = count + 1
    # Set up the eating apple part!
    if char.colliderect(char1):
        score = score + score_plus
        y = y
        x = x
        y_c = 0
        x_c = 0
        x_leaf = random.randint(0, 660)
        y_leaf = random.randint(0, 660)
    if char.colliderect(ob1):
        lives = lives - 20
        # Leave the game at you like it or not
    if keys[pygame.K_ESCAPE]:
        print("Your score is: " + str(score))
        running = False
    # Go back to your oranigal postion
    if keys[pygame.K_g]:
        y = 0
        lives = lives - 1
        x = 0
        x_c = 0
        y_c = 0
    if lives == 0 or 0 > lives:
        running = False
        print("You lost! You died!")
    # WIN!!!!!
    if score == 100 or score > 100:
        red = pygame.Color(0, 204, 102)
        winner = font.render("You win! Your score is: " + str(score) + " Press Esc to leave! Or click the Exit button!", True, (0, 0, 0))
        Window.blit(winner, (0, 350))
    # How hard it is
    if Setter == "1":
        if y == 640 or y == -640 or x == 640 or x == -640:
            lives -= 1
            if lives == 3:
                running = False
                print("You lost!")

    if Setter == "3":
        if y == 740 or y == -740 or x == 740 or x == -740:
            y = 0
            x = 0
            x_c = 0
            y_c = 0
    # Display score
    textY = 10
    textX = 10
    
    # Show the score
    score_shower = font.render("Score: " + str(score) + " Get 100 points to win! Speed: " + str(Speed_snake) + " Lives: " + str(lives) + " Time Left: " + str(Time), True, (0, 0, 0))
    Window.blit(score_shower, (15, 30))

    # NameTag
    name_y = y - 30
    name_x = x + 5
    nametag = NameTag_font.render(Name, True, (0, 0, 0))
    Window.blit(nametag, (name_x, name_y))

    if Speed_snake < 15:
        Speed_snake = 15
    if ob1x > 700:
        ob1x = 350
    if ob1y > 700:
        ob1y = 350
    if running == False:
        f = open("SnakeGameScores.txt", "a")
        f.write("You got this score on " + str(today) + ". Here is the score: " + str(score))
    if Time == 100:
        running = False
        print("You lost! The 100 seconds time limit is over.")





    # update the screen
    pygame.display.update()
pygame.quit()
# Make sure pygame does not use wasted rescouses
# To Make a log file
if running == True:
    fd = open("Log.txt", "a")
    fd.write("Your game started up on " + str(today))


