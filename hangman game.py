import random

import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

countries = ["canada","japan","mexico","spain","france","italy","australia","poland","ukrain","palestine","germany","united kingdom","united states","south africa","north korea","south korea","new zealand"]
colours = ["blue","red","green","yellow","orange","pink","teal","purple","black","white","grey"] 
sports = ["football","cricket","basketball","hockey","tennis","boxing","volleyball"]
theme = input(""" 1. Countries
 2. Colours
 3. Sports
 Pick a theme (1-3): """)
if theme == "1":
    word = random.choice(countries)
elif theme == "2":
    word = random.choice(colours)
elif theme == "3":
    word = random.choice(sports)
else:
    print(" Not a valid theme")

guessed = ""
letters_tried = []
for char in word:
    if char == " ":
        guessed += " "
    else:
        guessed += "_"

def draw_hangman(chances):
    if chances == 7:
        turtle.home()
        turtle.pendown()
        turtle.left(90)
        turtle.forward(175)
        turtle.left(90)
        turtle.forward(74)
        turtle.left(90)
        turtle.forward(35)
        turtle.penup()
        turtle.goto(-135,-35)
    if chances == 6:
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15,None,100)
        turtle.penup()
    elif chances == 5:
        # draw torso
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif chances == 4:
        # draw first arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif chances == 3:
        # draw second arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif chances == 1:
        # draw first leg
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif chances == 0:
        # draw second leg
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

def check_letter(guessed_letter,guessed):
    index = -1
    for letter in word:
        index += 1
        if guessed_letter == letter:
            guessed = guessed[:index] + letter + guessed[index + 1:]
    return guessed
        
chances = 8
while chances != 0:
    if guessed[0] != "_":
        print("""
 The word:""", guessed.capitalize())
    else:
        print("""
 The word:""", guessed)
    print(" Letters tried so far:", letters_tried)
    if word == guessed:
        chances = 0
    guessed_letter = input(" Enter a letter: ")
    guessed_letter = guessed_letter.lower()
    if guessed_letter in letters_tried:
        print(RED, "You already entered that letter", RESET)
    elif len(guessed_letter) != 1 or guessed_letter == " ":
        print(" Please enter 1 letter")
    elif len(guessed_letter) == 1:
        updated_guessed = check_letter(guessed_letter,guessed)
        if updated_guessed == guessed:
            print(RED, "Letter not found", RESET)
            chances -= 1
            print(" You have", chances, "chances left")
            draw_hangman(chances)
        else:
            print(GREEN, "Letter found", RESET)
        guessed = updated_guessed
        letters_tried += guessed_letter
        if word == guessed:
            chances = 0

if guessed == word:
    print(GREEN, "You won! The word was in fact", word.capitalize(), RESET)
else:
    print(RED, "You lost. The word was", word.capitalize(), RESET)


