"""
name = input('Enter a name: ')      #user input
name = name.capitalize().strip()    #fist letter of input apitalized

for n in range(len(name)):          #for each letter in the input
    print(name[n])                  #print the letter
"""

"""
name = input('Enter a name: ')      #user input
name = name.capitalize().strip()    #fist letter of input apitalized

for l in name:                      #for each letter in the input
    print(name[l])                  #print the letter
"""

"""
s = 'It was a bright cold day in April, and the clocks were striking thirdteen.'
print(s[:s.index(',')])             #print everything up to the ','
"""

"""
s = 'A screaming comes across the sky.'
print(s.replace('s','$'))           #replace every instance of 's' with '$'
"""

"""
tv = ['GOT', 'Narcos', 'Vice']
coms = ['Friends', 'Seinfeld', 'Simpsons']
all_shows = []

for show in tv:
    show = show.upper()             #all characters in caps
    all_shows.append(show)          #add to all_shows list

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
"""

"""
numbers_list = ['1', '2', '3', '4', '5']

while True:
    if len(numbers_list) > 0:
        print('press q to end the guessing')

        guess = input('Please guess a number: ')
        if guess == 'q':
            break
        elif guess in numbers_list:
            numbers_list.remove(guess)
            print(numbers_list)
            print('you got one!')
        else:
            print('no luck, try again')
    else:
        print('you got them all')
        break
"""

"""
x = 10

while x >= 0:
    print (x)
    x -= 1
"""

"""
import statistics

aList = [1,2,2,3]

print (statistics.mean(aList))
"""

"""
import os
os.path.join("Users", "bob", "st.txt")          # creating os specific file path structure
"""

"""
st = open("st.txt", "w")                        # open/create file (w=write,r=read,w+=read nd write)
st.write("hi from Python!")                     # write into the file
st.close()                                      # if you open a file you must close it
"""

"""
with open('st.txt', 'r') as 'f':
    f.write('hello my little world')
"""


import random

word_list = ['magenta', 'house', 'tire', 'elephant', 'water']
number_random = random.randint(0, len(word_list)-1)
word_selection = word_list[number_random]

print (word_selection)

