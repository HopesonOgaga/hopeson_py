secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('enter number: '))
    guess_count += 1
    guess_message = 'you win'
    if guess == secret_number:
        print(guess_message)
        break
else:
    print('sorry you failed')
