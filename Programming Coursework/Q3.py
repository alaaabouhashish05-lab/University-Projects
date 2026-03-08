#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:11:38 2024

@author: tylerkim
"""
    
import turtle
import time
import random
import os
from PIL import Image

wn = turtle.Screen()

death = "Q3-death.py"
win = "Q3-win.py"


#Importing images for sprites and background


bacteria = "~/Downloads/Sprites/bacteria1.png"
redbloodcell = "~/Downloads/Sprites/redbloodcell1.png"
whitebloodcell = "~/Downloads/Sprites/whitebloodcell1.png"
background = "~/Downloads/Sprites/background1.png"

bacteria = Image.open(os.path.expanduser(bacteria))
redbloodcell = Image.open(os.path.expanduser(redbloodcell))
whitebloodcell = Image.open(os.path.expanduser(whitebloodcell))

bacteria_gif = "bacteria.gif"
redbloodcell_gif = "redbloodcell.gif"
whitebloodcell_gif = "whitebloodcell.gif"

bacteria.save(bacteria_gif, "GIF")
redbloodcell.save(redbloodcell_gif, "GIF")
whitebloodcell.save(whitebloodcell_gif, "GIF")

turtle.register_shape(bacteria_gif)
turtle.register_shape(redbloodcell_gif)
turtle.register_shape(whitebloodcell_gif)


# Set the desired (x, y) position on the background image
x_position = -400
y_position = -300





# I'm givng each item a different bounce angle so that every game would be different and that there would 
Player_angle = random.randint(40, 80)
civ_angle = random.randint(40, 80)
Enemy_angle = random.randint(40, 80)
print("Bounce angle for Player is: ", Player_angle)
print("Bounce angle for Civillians is: ", civ_angle)
print("Bounce angle for Enemies is: ", Enemy_angle)

# Background
wn.bgpic(os.path.expanduser(background))
wn.setup(1000,750)
wn.screensize(1000, 750)
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(3)

# Create Sprite class for objects within the game, inherit turtle.Turtle attributes
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):  # Initialiser for Sprite class and applies to all its subclasses
        turtle.Turtle.__init__(self, shape=spriteshape)
        # Settings for all subclasses of Sprite class
        self.speed(0)
        self.penup()  # Disables drawing
        self.color(color)
        self.goto(startx, starty)
        self.speed_val = 1  # Each sprite has an initial speed 1

    def move(self):
        self.fd(self.speed_val)


# Create new Subclass of Sprite 'Player'
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # Initialising all atributes used later on
        self.player_speed = 3  # Base speed
        self.base_speed = 3  # Speed after boosting
        self.lives = 3
        self.boost_duration = 0.3
        self.boost_start_time = 0
        self.is_boosting = False  # Boost state normally
        self.boost_cooldown = 3
        self.last_boost_time = 0  # Adds ability to store time last boosted so can have a cool down
        # Add boost monitor bar
        self.boost_bar = turtle.Turtle()
        self.boost_bar.shape("square")
        self.boost_bar.shapesize(stretch_wid=0.01, stretch_len=0.01)
        self.boost_bar.color("green")
        self.boost_bar.penup()
        self.boost_bar.goto(-400, -350)


    # Player control settings
    def turn_left(self):
        self.lt(30)

    def turn_right(self):
        self.rt(30)

    def accelerate(self):
        self.player_speed = 5

    def deccelerate(self):
        self.player_speed = -5

    def stop(self):
        self.player_speed = 0

    # Boost ability
    def start_boost(self):
        current_time = time.time()
        if not self.is_boosting and (current_time - self.last_boost_time >= self.boost_cooldown):
            self.player_speed = 20
            self.is_boosting = True
            self.boost_start_time = current_time  # Starts recording time data needed for cooldown
            self.last_boost_time = current_time

    def apply_boost(self):
        if self.is_boosting:
            if time.time() - self.boost_start_time >= self.boost_duration:  # Math for boost duration
                self.player_speed = self.base_speed
                self.is_boosting = False
                
    
# Call the function to draw "Boost"

            
    # Boost bar
    def update_boost_bar(self):
        current_time = time.time()
        # Math for boost bar
        time_elapsed = current_time - self.last_boost_time
        cooldown_remaining = max(0, self.boost_cooldown - time_elapsed)
        cooldown_percentage = cooldown_remaining / self.boost_cooldown
        if cooldown_percentage == 0:
            cooldown_percentage = 0.01

        self.boost_bar.shapesize(stretch_len=cooldown_percentage * 7.5, stretch_wid=0.3)

    def reset(self):
        self.goto(0, 0)
        self.player_speed = 0

    def move(self):
        self.apply_boost()
        self.fd(self.player_speed)

        # Check for collisions with civilians
        for civilian in civilians:
            if self.distance(civilian) < 20:
                turtle.bye()
                os.system(death)
                    

        # Check for collisions with enemies
        for enemy in enemies:
            if self.distance(enemy) < 20:
                enemy.ht()
                enemies.remove(enemy)

        if self.xcor() > 495:
            self.rt(Player_angle)
            self.setx(495)
        if self.xcor() < -495:
            self.rt(Player_angle)
            self.setx(-495)
        if self.ycor() > 370:
            self.rt(Player_angle)
            self.sety(370)
        if self.ycor() < -370:
            self.rt(Player_angle)
            self.sety(-370)

# Subclass for civilians
class Civilians(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.civilian_speed = 2
        self.setheading(random.randint(0, 306))

    def move(self):
        self.fd(self.civilian_speed)
        if self.xcor() > 495:
            self.rt(civ_angle)
            self.setx(495)
        if self.xcor() < -495:
            self.rt(civ_angle)
            self.setx(-495)
        if self.ycor() > 370:
            self.rt(civ_angle)
            self.sety(370)
        if self.ycor() < -370:
            self.rt(civ_angle)
            self.sety(-370)

# Subclass for enemies
class Enemies(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.enemy_speed = 5
        self.setheading(random.randint(0, 306))

    def move(self):
        self.fd(self.enemy_speed)
        if self.xcor() > 495:
            self.rt(Enemy_angle)
            self.setx(495)
        if self.xcor() < -495:
            self.rt(Enemy_angle)
            self.setx(-495)
        if self.ycor() > 370:
            self.rt(Enemy_angle)
            self.sety(370)
        if self.ycor() < -370:
            self.rt(Enemy_angle)
            self.sety(-370)

# Class for the game
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.lives = 3
        self.pen = turtle.Turtle()
    
    def enemy_count(self):
        return len(enemies)


    # Draw the border
    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(5)
        self.pen.penup()
        self.pen.goto(-500, 375)
        self.pen.pendown()
        self.pen.fd(1000)
        self.pen.rt(90)
        self.pen.fd(750)
        self.pen.rt(90)
        self.pen.fd(1000)
        self.pen.rt(90)
        self.pen.fd(750)
        self.pen.penup()
        self.pen.ht()


# Initialize game
game = Game()
game.draw_border()


# Create multiple instances of Player, Civilian, and Enemies
player = Player(whitebloodcell_gif, "white", 0, 0)
civilians = [Civilians(redbloodcell_gif, "blue", random.randint(-500, 500), random.randint(-370, 370)) for _ in range(3)]
enemies = [Enemies(bacteria_gif, "red", random.randint(-500, 500), random.randint(-370, 370)) for _ in range(7)]


# Set up key bindings
turtle.onkey(player.turn_left, "a")
turtle.onkey(player.turn_right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.deccelerate, "s")
turtle.onkey(player.start_boost, "space")
turtle.onkey(player.reset, "r")
turtle.listen()


# Main game loop
screen = turtle.Screen()
while True:
    player.move()
    for civilian in civilians:
        civilian.move()
    for enemy in enemies:
        enemy.move()
    if game.enemy_count() == 0:
        turtle.bye()
        os.system(win)
    turtle.Screen().update()
    player.update_boost_bar()
    time.sleep(0.01)

