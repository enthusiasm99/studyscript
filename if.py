number = 23
guess = int(input('Input an integer:'))
if guess == number:
    print('You are right!')
elif guess > number:
    print('Input smaller an integer')
else:
    print('Input bigger an integer')
print('Game over')