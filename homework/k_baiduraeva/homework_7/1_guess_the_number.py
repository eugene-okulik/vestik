secret_num = 21

while True:
    num = int(input('Guess the number: '))
    if num == secret_num:
        break
    else:
        print('Try again')

print('Congrats! You guessed the number!')
