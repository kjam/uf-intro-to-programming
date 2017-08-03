from sys import argv


def chatty(username):
    print('Hi %s! Thanks for joining!' % username)
    color = input('What is your favorite color? ')
    print('Oh neat! I like {} too!'.format(color))
    print('Pick a number 1 to 10.')
    number = input('(1-10): ')
    while True:
        if number.isnumeric() and int(number) >= 1 and int(number) <= 10:
            print('Great job, %s! \U0001F389' % username)
            return
        else:
            print('Hmmm... \U0001F914 Try again!')
            number = input('(1-10): ')


if __name__ == '__main__':
    username = argv[1]
    chatty(username)
