from flask import Flask, render_template
from pathlib import Path
import Utils

app = Flask(__name__)


@app.route('/')
def home():
    try:
        scores_file = open(Path('Scores.txt'), 'r')
        score = scores_file.read()
        return render_template('score.html', SCORE=score)
    except FileNotFoundError:
        error = Utils.BAD_RETURN_CODE

        return render_template('error.html',ERROR=error)



if __name__ == '__main__':
    app.run()
