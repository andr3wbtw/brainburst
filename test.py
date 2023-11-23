import pygame
from pygame.locals import*
import pickle
import random

#Function to generates random word
def randomWord():
    # opens text file
    my_file = open("dictionary/fruits.txt", "r") 
  
    # reads the text file 
    data = my_file.read() 

    # replacing end splitting the text  
    # when newline ('\n') is seen. 
    wordList = data.split("\n") 
    my_file.close() 
    
    # generate random word from list
    randomValue = random.randint(0,len(wordList)-1)
    return(wordList[randomValue])

print(randomWord())