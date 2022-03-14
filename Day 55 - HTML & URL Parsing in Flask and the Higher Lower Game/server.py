from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<img src="https://media.giphy.com/media/4JVTF9zR9BicshFAb7/giphy.gif">'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess == random_num:
        return "<h1 style='color: green'>Well done! You've won something! Your life isn't pointless anymore</h1>" \
               "<img src='https://media.giphy.com/media/nV92wySC3iMGhAmR71/giphy.gif'>"
    elif guess > random_num:
        return "<h1 style='color: red'>Too high! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/d8EN0mls2eoAFLRiX8/giphy.gif'>"
    elif guess < random_num:
        return "<h1 style='color: purple'>Too low! Try again!</h1>" \
               "<img src='https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif'>"





if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
