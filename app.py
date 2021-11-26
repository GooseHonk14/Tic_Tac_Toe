from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'POST':
        return redirect('https://5000-lavender-crocodile-z392xfsm.ws-us17.gitpod.io/game/update/{{id}}')
    return render_template('game.html')


@app.route('/game/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    