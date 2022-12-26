import time


def generate_number(koshi):  # פונקציה שמגנרטת מספר רנדומלי בין 1 לרמת הקושי שהמשתמש בחר
    import random  # ספריית random
    secret_number = int(random.uniform(1, koshi))  # המשתנה secret_number מכניסים אותו בתור int מ1 עד רמת הקושי
    return secret_number


def get_guess_from_user(koshi):  # פונקציה שנותנת למשתמש לנחש מספר בין 1 לרמת הקושי
    user_num = int(
        input(f'guess number between 1 and {koshi}: '))  # משתנה user_num בו היוזר מכניס משתמש בין 1 ל רמת הקושי
    return user_num


def compare_result(secret_number, user_num):  # פונקציה אשר משווה בין generate_number לget_guess_from_user
    if secret_number == user_num:  # אם המספר בפונקציה הראשונה שווה למספר שהכניס המשתמש בפונקציה השניה החזר True
        return True


def play(koshi):  # הפונקציה שמפעילה את המשחק
    secret_number = generate_number(koshi)  # פה מתבצעת הכנסת המספר הסודי דרך הפונקציה הראשונה שעושה random
    print('generating...')  # הדפסה בשביל המשתמש
    time.sleep(2)  # המתנה של 2 שניות
    print('ready?')  # הדפסה של המשתמש
    time.sleep(2)  # הדפסה של 2 שניה

    user_num = get_guess_from_user(koshi)  # פה מתבצעת ההכנסה של המספר שהיוזר בחר

    while True:
        if compare_result(secret_number=secret_number, user_num=user_num): # פונקציית ההשוואה מתבצעת כשהvalue של כל
            # אחד מהפונקציות נכנס לתוך משתנה
            print('correct!')
            break
        else:
            print('nope')
            return False
