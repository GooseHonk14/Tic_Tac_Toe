from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
   return render_template('game.html')


@app.route('/game/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':  
       newthing = id
    return newthing

if __name__ == '__main__':
    app.run(debug=True)
    