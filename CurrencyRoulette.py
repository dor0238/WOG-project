from currency_converter import CurrencyConverter


def get_money_interval(koshi):
    import random
    random_num = int(random.uniform(1, 100))
    c = CurrencyConverter()
    t = c.convert(random_num, 'USD', 'ILS')
    low = int(t - (5 - koshi))
    high = int(t + (5 - koshi))

    return t, low, high


def get_guess_from_user(t):
    while True:
        try:
            guess = int(input(f'enter {t} in ILS: '))
        except ValueError:
            print('enter numbers')
            continue

        return guess


def play(koshi):
    t, low, high = get_money_interval(koshi)
    guess = get_guess_from_user(t)
    if high >= guess >= low:
        print('victory!')
        return True
    else:
        print('you wrong, loser')
        return False

