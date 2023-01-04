def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        with open("Scores.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        score = 0


    scores =+ POINTS_OF_WINNING

    with open("Scores.txt","w") as f:
        f.write(str(scores))


