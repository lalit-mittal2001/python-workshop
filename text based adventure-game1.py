#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#KUNAL KUNDU ,ROLL-NO:2K18CSUN01110,B-TECH:CSE-4A
#LALIT MITTAL,ROLL-NO:2K18CSUN01111,BTECH:CE-4A
#TOPIC:TEXT BASED ADVENTURE GAME 


# In[1]:



#The term "Adventure game" originated from the 1970s text computer game Colossal Cave Adventure, 
often referred to simply as Adventure, which pioneered a style of gameplay that was widely imitated and became a genre in its own right. ... 
Essential elements of the genre include storytelling, exploration, and puzzle solving.

#Adventure games contain a variety of  puzzle decoding messages, finding and using items, opening locked doors,
or finding and exploring new locations. Solving a puzzle will unlock access to new areas in the game world,
and reveal more of the game story. Logic puzzles, where mechanical devices are designed with abstract interfaces to test a player's deductive reasoning skills, are common.
import random
import time

def displayIntro():
    print("Topic:  TEXT-Based Adventure Game")
    print("Python is an interpreted, high-level, general-purpose programming language.")
    print("Python is considered a scripting language.")
    
    
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")




# In[ ]:




