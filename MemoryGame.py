import time
import os


def generate_memory(koshi):
    import random
    print('Welcome to the memory game!')
    time.sleep(4)
    print('i will show you random numbers between 1 - 100, remeber them!')
    time.sleep(3)
    print('ready?')
    print('3')
    time.sleep(2)
    print('2')
    time.sleep(2)
    print('1.....')
    print('Good Luck')
    time.sleep(1)

    random_num = []  # המספרים הרנדומליים יכנסו לlist
    for number in range(koshi):  # לולאת for שמכניסה מספרים לlist לפי רמת הקושי שנבחרה
        random_num.append(int(random.uniform(1, 101)))  # הכנסת המספרים לרשימה,כמות המספרים נמדדת ברמת הקושי והמספרים
        # הם בין 1 ל99

    print(random_num)
    time.sleep(3)
    os.system('clear')
    return random_num


def user_input(koshi):
    user_list = []
    print(f'Please enter {koshi} numbers: ')
    for i in range(koshi):
        i = user_list.append(int(input('insert number : ')))
    return user_list


def compare_list(random_num, user_list):
    while True:
        if random_num == user_list:
            print('correct!')
            break
        else:
            'failed!'
            return False


def play(koshi):
    random_num = generate_memory(koshi)
    user_list = user_input(koshi)
    if compare_list(random_num=random_num, user_list=user_list):

        print('correct!')
        return True

    else:
        return False
