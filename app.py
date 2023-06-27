from flask import Flask, render_template, request

app = Flask(__name__)

alunos = [
    {
        'id': 1,
        'nome': 'Lucas',
        'idade': 22,
        'curso': 'Sistemas'
    },
    {
        'id': 2,
        'nome': 'Luan',
        'idade': 20,
        'curso': 'Sistemas'
    },
    {
        'id': 3,
        'nome': 'Kayky',
        'idade': 20,
        'curso': 'Sistemas'
    }
]

# Rota inicial
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Rota para exibir a lista de alunos
@app.route('/alunos')
def listar_alunos():
    return render_template('alunos.html', alunos=alunos)

# Rota para cadastrar um novo aluno
@app.route('/cadastro-alunos', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        curso = request.form['curso']
        novo_aluno = {
            'id': len(alunos) + 1,
            'nome': nome,
            'idade': idade,
            'curso': curso
        }
        alunos.append(novo_aluno)
        return render_template('aluno.html', aluno=novo_aluno)
    return render_template('cadastro_alunos.html')

# Rota para exibir informações de um aluno específico
@app.route('/ver-aluno/<int:id>')
def ver_aluno(id):
    aluno = None
    for a in alunos:
        if a['id'] == id:
            aluno = a
            break
    return render_template('aluno.html', aluno=aluno)

if __name__ == '__main__':
    app.run(debug=True)
