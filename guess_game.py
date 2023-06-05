guess_limit = 3
secret_number = 9
guess_count = 0
while guess_count <= guess_limit:
    guess = int(input('guess number: '))
    guess_count += 1
    message = 'you win'
    if guess == secret_number:
        print(message)
        break
else:
    print('try again')
