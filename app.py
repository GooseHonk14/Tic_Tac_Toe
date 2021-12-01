from flask import Flask, render_template, request, redirect
app = Flask(__name__)
x = "X"
o = "O"
blank = " "
board = [[blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank]]

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'POST':
        user_input = int(request.form["button"])
        if user_input == 1:
            board[0][0] = x
        elif user_input == 2:
            board[0][1] = x
        elif user_input == 3:
            board[0][2] = x
        elif user_input == 4:
            board[1][0] = x
        elif user_input == 5:
            board[1][1] = x
        elif user_input == 6:
            board[1][2] = x
        elif user_input == 7:
            board[2][0] = x
        elif user_input == 8:
            board[2][1] = x
        elif user_input == 9:
            board[2][2] = x
        else:
            return "Something went wrong"
    else:
        return render_template('game.html', board = board)



if __name__ == '__main__':
    app.run(debug=True)
    