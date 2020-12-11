"""
name = input('Enter a name: ')      #user input
name = name.capitalize().strip()    #fist letter of input apitalized

for n in range(len(name)):          #for each letter in the input
    print(name[n])                  #print the letter
"""

s = 'It was a bright cold day in April, and the clocks were striking thirdteen.'
print(s[:s.index(',')])
