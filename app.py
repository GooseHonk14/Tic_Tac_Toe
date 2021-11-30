from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'POST':
        if request.form["button"] == 1:
            return "It worked"
        elif request.form["button"] == '1':
            return "It worked as a string"
        else:
            return "it didn't work"
    else:
        return render_template('game.html')



if __name__ == '__main__':
    app.run(debug=True)
    