from pathlib import Path


def add_score(koshi):
    POINT_OF_WINNING = str((koshi * 3)+ 5)

    try:
        score_file = open(Path('Scores.txt'),'r')
        score = open(Path('Scores.txt'),'a')
        score.write(f''',{POINT_OF_WINNING}''')
    except FileNotFoundError:
        score = open(Path('Scores.txt'),'x')
        score.write(POINT_OF_WINNING)