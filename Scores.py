def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5  # Calculating score
    try:
        with open("Scores.txt", "r") as f:  # Read file "Scores"
            score = int(f.readline())  # Read the first line of "Scores.txt"
    except FileNotFoundError:  # if the file doesn't exist, create the file and set the score to 0
        score = 0

    score += POINTS_OF_WINNING  # adds the point of the current score

    with open("Scores.txt", "w") as f:  # overwrite the score in the file
        f.write(str(score))
