import MemoryGame
import GuessGame
import CurrencyRoulette

global koshi, choose


def welcome():
    user = input('Please enter your name: ')
    print(f'''
    Hello {user} and welcome to the World of Games (WoG).
    Here you can find many cool games to play.
    ''')
    return user


def load_game():
    print('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    while True:
        try:
            choose = int(input('please choose a game between 1-3 '))
            while 3 < choose or choose < 1:
                choose = int(input('please choose a game between 1-3'))
            koshi = int(input('please choose difficulty between 1 - 5'))
            while 5 < koshi or koshi < 1:
                koshi = int(input('please choose difficulty between 1 - 5'))
        except ValueError:
            print('Enter only numbers')
            continue
        if choose == 1:
            MemoryGame.play(koshi)

        elif choose == 2:
            GuessGame.play(koshi)

        elif choose == 3:
            CurrencyRoulette.play(koshi)
