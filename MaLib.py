import os
import requests
import shutil
import sys
import time

os.system('cls')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


# Story base is refrence for myself!
def storyBase():
    print('A Normal day in Tanque Verde high school looks like [ADJECTIVE1]. Most people are [NOUN1] as they are doing [VERB1] in the mornings. ' \
    'Math is an [ADJECTIVE2] class while English is an [ADJECTIVE3] class. People during lunch are [ACTION1] and talking to their friends. They are eating [FOOD1] and [FOOD2].' \
    'After school, students can be found doing [VERB2]. Most school days in students [ADJECTIVE4] outside the school.')

def printDelay(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures the character is immediately displayed
        time.sleep(delay)
    print() # Add a newline at the end

def welcome():
    printDelay('\x1b[35mA Day in Tanque Verde High School: A Malib', 0.1)
    printDelay('\033[96mWelcome! You are about to play malib where you will, most likely, die in laughter\033[00m', 0.01)
    printDelay('\033[96mPlease answer the following questions where a story will be made that could be, very messed up, or very good\033[00m', 0.01)
    print()

def easterEggs(prompt):
    if prompt == 'pancake':
        os.system('start chrome "https://media.istockphoto.com/id/161170090/photo/pancakes-with-berries-and-maple-syrup.jpg?s=612x612&w=0&k=20&c=8EctScsN7q5UmxeXPNBnYN1eFmJmgmp2bE0OIq_czwM="')
    if prompt == 'cfderx3wcfr43vgt5hy65hy':
        os.system('start chrome')
        os.system('start chrome "https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1"')    
    if prompt == 'silas':
        print('silas is cringe')
        quit()

def questions():
    print('\x1b[33mPlease provide a ADJECTIVE: \033[00m')
    adjective1 = str(input('\x1b[36m'))
    easterEggs(adjective1)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a NOUN: \033[00m')
    noun1 = str(input('\x1b[36m'))
    easterEggs(noun1)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a VERB: \033[00m')
    verb1 = str(input('\x1b[36m'))
    easterEggs(verb1)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide an ADJECTIVE: \033[00m')
    adjective2 = str(input('\x1b[36m'))
    easterEggs(adjective2)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide an ADJECTIVE: \033[00m')
    adjective3 = str(input('\x1b[36m'))
    easterEggs(adjective3)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a ACTION: \033[00m')
    action1 = str(input('\x1b[36m'))
    easterEggs(action1)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a FOOD: \033[00m')
    food1 = str(input('\x1b[36m'))
 #   easterEggs(food1)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a FOOD: \033[00m')
    food2 = str(input('\x1b[36m'))
 #   easterEggs(food2)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide a VERB: \033[00m')
    verb2 = str(input('\x1b[36m'))
    easterEggs(verb2)
    os.system('cls')
    welcome()

    print('\x1b[33mPlease provide an ADJECTIVE: \033[00m')
    adjective4 = str(input('\x1b[36m'))
    easterEggs(adjective4)
    os.system('cls')
    welcome()

    return adjective1, adjective2, adjective3, adjective4, food1, food2, action1, noun1, verb1, verb2

welcome()
adjective1, adjective2, adjective3, adjective4, food1, food2, action1, noun1, verb1, verb2 = questions()
print('\033[32mHere is your story:')
print('\033[00mA Normal day in Tanque Verde high school looks like ' + '\033[31m' + str(adjective1) + '\033[00m'+ '. Most people are ' + '\033[31m' + str(noun1) + '\033[00m'+ ' as they are doing ' \
      + '\033[31m' + str(verb1) + '\033[00m'+ ' in the mornings. ''Math is an ' + '\033[31m' + str(adjective2) + '\033[00m'+' class while English is an ' + '\033[31m' + str(adjective3) + '\033[00m'+ ' class. People during lunch are ' + '\033[31m' + str(action1) + '\033[00m'+ \
      ' and talking to their friends. They are eating ' + '\033[31m' +  str(food1) + '\033[00m'+ ' and '+ '\033[31m' +  str(food2) + '\033[00m'+'.' \
    ' After school, students can be found doing ' + '\033[31m' + str(verb2) + '\033[00m'+ '. Most school days in students ' + '\033[31m' + str(adjective4) + '\033[00m'+ ' outside the school. ')
