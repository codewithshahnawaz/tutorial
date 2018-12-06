from random import *
names = ['hospital', 'linux', 'android', 'fedora', 'word', 'helicopter']
shuffle(names)
display = []
display.extend(list(names[0]))
for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()
count = 0
while count < len(list(names[0])):
    guess = input('Please guess a %d letter: '% len(list(names[0])))
    guess = guess.lower()
    print(count)
    for i in range(len(list(names[0]))):
        if list(names[0])[i] == guess:
            display[i] = guess
            count += 1
    print(' '.join(display))
    print()
print("Well done,you guessed the word")
feedback = input('Do you like this game [y]n')
if feedback == 'y' or feedback == 'yes'or  feedback == 'Yes':
    print('Thanks for feedback!!!')
else:
    print('Ok we will try to improve this project!')
print("Thanks for playing")
