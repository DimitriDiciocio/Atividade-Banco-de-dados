from flask import Flask, redirect, render_template, request
app = Flask(__name__)

games =[]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', games=games)

@app.route('/adicionar_games', methods=['GET', 'POST'])
def adicionar_games():
    if request.method == 'POST':
        name = request.form['name']
        genre = request.form['genre']
        genre = genre.capitalize()
        name = name.capitalize()
        code = len(games)
        if name == "" or genre == "":
            erro = "Erro! Algum dado não foi preenchido corretamente"
            return render_template('adicionar_games.html', erro = erro)
        games.append([code, name, genre])
        return redirect('/')
    else:
        return render_template('adicionar_games.html', games=games)

@app.route('/editar_games/<int:code>', methods=['GET', 'POST'])
def editar_games(code):
    if request.method == 'POST':
        name = request.form['name']
        genre = request.form['genre']
        genre = genre.capitalize()
        name = name.capitalize()
        games[code] = [code, name, genre]
        return redirect('/')
    else:
        game = games[code]
        return render_template('editar_games.html', game=game)

@app.route('/apagar_games/<int:code>')
def apagar_games(code):
    del games[code]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)