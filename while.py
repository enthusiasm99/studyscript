number = 23
running = True
while running:
    guess = int(input('Input an integer:'))
    if guess == number:
        print('Congratulations!You are right')
        running = False
    elif guess < number:
        print('Input a bigger integer:')
    else:
        print('Input a smaller integer:')
else:
    print('The while loop is over.')
print('Game over')