import random 
import time

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    num_guesses = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print('Invalid value, please input a number')
            continue
        num_guesses += 1
        if guess < random_number:
            print('Sorry, please guess again. Your guess is too low.')
        elif guess > random_number:
            print('Sorry, please guess again. Your guess is too high.')
        if num_guesses == 5:
            print('Sorry, you have reached the maximum number of guesses.')
            break
    if guess == random_number:
        print(f'Wunderbar, congrats. You have guessed the number {random_number} correctly!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    start_time = time.time()
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #it could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? Or do you want to quit (Q)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'q':
            break
        if time.time() - start_time >= 5:
            print('Sorry, you have run out of time.')
            break
    if feedback == 'c':
        print(f'Yay! The computer guessed your number, {guess}, correctly!')

print('Welcome to the number guessing game!')
print('Select an option:')
print('1. Human guesses the number')
print('2. Computer guesses the number')
print('3. Quit')
option = input('Enter option number: ')
while option != '3':
    if option == '1':
        guess(15)
    elif option == '2':
        computer_guess(10)
    else:
        print('Invalid option')
    print('Select an option:')
    print('1. Human guesses the number')
    print('2. Computer guesses the number')
    print('3. Quit')
    option = input('Enter option number: ')
print('Thanks for playing!')
