from flask import Flask, request, render_template, make_response, send_file, jsonify, flash, redirect, session
from flask_session import Session
import random
from fractions import Fraction
from reportlab.pdfgen import canvas
from io import BytesIO
import json
from helpers import gerar_fracoes_unicas, gerar_numero_decimal, decimal_para_fracao_irredutivel
from werkzeug.security import generate_password_hash, check_password_hash
import os, secrets, string
from cs50 import SQL

# Iniciar aplicação flask
app = Flask(__name__, static_folder="static")
SECRET_KEY = 'U7^GL4RuH$d^LWaHTAs9!O4Fu'

# Configurações básicas do app
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = SECRET_KEY
app.template_folder = 'templates'
Session(app)

@app.context_processor
def inject_user_logged_in():
    return dict(user_logged_in='user_id' in session)

# Iniciar base de dados para aplicação
db = SQL("sqlite:///bingo.db")

CREATE_TABLE_PROFESSOR = """
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);


"""

CREATE_TABLE_JOGOS = """
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    numeros_disponiveis TEXT NOT NULL,
    numeros_sorteados TEXT NOT NULL,
    professor_id INTEGER NOT NULL,
    tipo_cartela TEXT NOT NULL,
    FOREIGN KEY(professor_id) REFERENCES professor(id)
);


"""

def init_db():
    db.execute(CREATE_TABLE_PROFESSOR)
    db.execute(CREATE_TABLE_JOGOS)

init_db()

# INÍCIO
@app.route('/', methods=['GET', 'POST'])
def inicio():
    user_logged_in = 'user_id' in session
    return render_template('index.html', user_logged_in=user_logged_in)

# REGISTRO, LOGIN E LOGOUT

# Verificar se o e-mail existe em bingo.db
def username_exists(email):
    existing_username = db.execute("SELECT email FROM professor WHERE email = :email", email=email)
    return len(existing_username) > 0

# Registro
@app.route("/register", methods=["GET", "POST"])
def registro():
    """Register user"""
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Verificar se o usuário digitou e-mail e senha
        if not email or not password:
            flash('Preencha todos os campos.')
            return render_template("register.html")

        # Verificar se o e-mail está disponível
        if username_exists(email):
            flash('E-mail já utilizado.')
            return render_template("register.html")

        # Inserir hash_password em bingo.db
        password_hash = generate_password_hash(password)
        db.execute("INSERT INTO professor (email, password) VALUES (:email, :password_hash)", email=email, password_hash=password_hash)

        # Logar o usuário depois de cadastro com sucesso
        rows = db.execute("SELECT * FROM professor WHERE email = :email", email=email)
        session["user_id"] = rows[0]["id"]
        return redirect("/geracao")

    return render_template("register.html")

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Esquecer qualquer user_id
    session.clear()

    if request.method == "POST":
        # Garantir que o usuário inseriu e-mail
        if not request.form.get("email"):
            flash('Insira um e-mail', 'error')
            return render_template("login.html")

        # Garantir que o usuário inseriu a senha
        elif not request.form.get("password"):
            flash('Insira a senha', 'error')
            return render_template("login.html")

        rows = db.execute("SELECT * FROM professor WHERE email = :email", email=request.form.get("email"))

        if len(rows) == 0:
            flash('E-mail não encontrado.')
            return render_template("login.html")

        password_check = check_password_hash(rows[0]["password"], request.form.get("password"))
        if not password_check:
            flash('Senha incorreta.')
            return render_template("login.html")

        # Logar o usuário
        session["user_id"] = rows[0]["id"]

        # Redirecionar usuário para página de jogos
        return redirect("/geracao")


    else:
        # Usuário acessou a rota via GET (como clicando em link ou via redirect)
        return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    """Log user out"""

    # Esquecer qualquer usuário
    session.clear()

    # Redirecionar para a página inicial
    return redirect("/")

# JOGAR
@app.route('/jogar')
def jogar():
    if 'user_id' in session:
        return redirect('geracao')
    else:
        return redirect('login')

#GERAÇÃO DE CARTELAS
@app.route('/geracao', methods=['GET', 'POST'])
def gerar_cartelas():
    cartelas = []

    if request.method == 'POST':
        nome_jogo = request.form.get('nomeJogo')
        num_cartelas = int(request.form.get('numCartelas'))
        tipo_cartelas = request.form.get('tipoCartelas')
        professor_id = session.get('user_id')

        # Inicializa números disponíveis para o sorteio
        numeros_disponiveis = []

        if nome_jogo:
            db.execute("""
                INSERT INTO jogos (nome, numeros_disponiveis, numeros_sorteados, professor_id, tipo_cartela)
                VALUES (:nome, :numeros_disponiveis, :numeros_sorteados, :professor_id, :tipo_cartela);
            """, nome=nome_jogo, numeros_disponiveis=json.dumps([]), numeros_sorteados=json.dumps([]), professor_id=professor_id, tipo_cartela=tipo_cartelas)

            novo_jogo_id = db.execute("SELECT LAST_INSERT_ROWID() as id;")[0]["id"]

            # Gere 74 números com base na escolha do usuário apenas se a lista estiver vazia
            if tipo_cartelas == "fracionarios":
                # Usa a função auxiliar para gerar a lista de números fracionários únicos
                numeros_disponiveis = gerar_fracoes_unicas(74)
            else:
                numeros_disponiveis = gerar_numero_decimal(74)

            # Atualiza o jogo recém-criado com os números gerados
            db.execute("""
            UPDATE jogos
            SET numeros_disponiveis = :numeros_disponiveis
            WHERE id = :jogo_id
            """, numeros_disponiveis=json.dumps(numeros_disponiveis), jogo_id=novo_jogo_id)

        for _ in range(num_cartelas):
            cartela = []

            # Escolhe 24 números únicos, dos 74 disponíveis, para formar a cartela
            numeros_unicos = random.sample(numeros_disponiveis, 24)

            for numero in numeros_unicos:
                cartela.append(numero)

            cartela.insert(12, "FREE")
            cartela = [cartela[i:i + 5] for i in range(0, len(cartela), 5)]
            cartelas.append(cartela)

        return render_template('cartelas.html', cartelas=cartelas)

    return render_template('geracao.html', cartelas=None)

# EXIBIÇÃO DAS CARTELAS GERADAS
@app.route('/cartelas', methods=['GET'])
def exibir_cartelas():
    return render_template('cartelas.html', cartelas=None)

# IMPRESSÃO DAS CARTELAS GERADAS
@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    # Recupera as cartelas dos dados do formulário
    cartelas = json.loads(request.form['cartelas'])

    # CriA um buffer de bytes para armazenar o PDF
    buffer = BytesIO()

    # InicializA o objeto Canvas do ReportLab
    c = canvas.Canvas(buffer)
    c.setPageSize((595, 842))  # Tamanho A4

    # DefinE as dimensões iniciais e o espaçamento
    x_init, y_init = 50, 820
    offset_coluna = 260  # Deslocamento entre colunas
    offset_linha = 250  # Deslocamento entre linhas
    tamanho_celula = 40  # Tamanho das células
    espaco_extra = 10  # Espaço extra para separação das linhas de cartelas

    coluna_count, linha_count = 0, 0

    for idx, cartela in enumerate(cartelas):
        x, y = x_init + coluna_count * offset_coluna, y_init - linha_count * (offset_linha + espaco_extra)

        # Desenha a borda externa da cartela englobando nome e número
        c.rect(x, y - (5 * tamanho_celula + 30), 5 * tamanho_celula, 5 * tamanho_celula + 30)

        # Desenha a grade da cartela
        for i in range(6):
            c.line(x, y - i * tamanho_celula - 30, x + 5 * tamanho_celula, y - i * tamanho_celula - 30)
        for j in range(6):
            c.line(x + j * tamanho_celula, y - 30, x + j * tamanho_celula, y - 5 * tamanho_celula - 30)

        # Escreve os números na cartela
        for i, linha in enumerate(cartela):
            x_temp = x
            for j, numero in enumerate(linha):
                c.drawCentredString(x_temp + tamanho_celula / 2, y - (i * tamanho_celula + tamanho_celula / 2 + 6) - 30, str(numero))
                x_temp += tamanho_celula

        # Adicione o número da cartela no canto superior direito
        c.drawRightString(x + 5 * tamanho_celula - 5, y - 22, f"#{idx + 1}")  # Ajustado para -15

        # Adicione um espaço no canto superior esquerdo para o nome
        c.drawString(x + 5, y - 23, "Nome: _____________")

        coluna_count += 1
        if coluna_count > 1:  # Ao completar 2 colunas de cartelas, vá para a próxima linha
            coluna_count = 0
            linha_count += 1
            if linha_count > 2:  # Ao completar 3 linhas de cartelas, comece uma nova página
                linha_count = 0
                c.showPage()  # Comece uma nova página no PDF

    # Salve o documento PDF
    c.save()

    # Reposicione o buffer para o início para a leitura
    buffer.seek(0)

    # Retorne o PDF como uma resposta
    response = make_response(send_file(buffer, as_attachment=True, download_name="cartelas.pdf", mimetype="application/pdf"))

    return response

#SORTEIO
@app.route('/sorteio', methods=['GET', 'POST'])
def pagina_sorteio():
    # Busque os jogos associados ao professor logado.
    jogos = db.execute("SELECT id, nome FROM jogos WHERE professor_id = :professor_id", professor_id=session.get("user_id"))

    # Se o método for POST, isso significa que o usuário selecionou um jogo e submeteu o formulário.
    if request.method == 'POST':
        jogo_id = request.form.get('jogoSelecionado')
        # Busca os números disponíveis e sorteados do jogo selecionado
        jogo_info = db.execute("SELECT numeros_disponiveis, numeros_sorteados, tipo_cartela FROM jogos WHERE id = :jogo_id", jogo_id=jogo_id)

        if jogo_info:
            numeros_disponiveis = json.loads(jogo_info[0]['numeros_disponiveis'])
            numeros_sorteados = json.loads(jogo_info[0]['numeros_sorteados'])
            tipo_cartela = jogo_info[0]['tipo_cartela']

            if numeros_disponiveis:
                numero_sorteado = random.choice(numeros_disponiveis)
                numeros_sorteados.append(numero_sorteado)
                numeros_disponiveis.remove(numero_sorteado)

                # Atualize o banco de dados com os novos conjuntos de números disponíveis e sorteados
                db.execute("UPDATE jogos SET numeros_disponiveis = :numeros_disponiveis, numeros_sorteados = :numeros_sorteados WHERE id = :jogo_id",
                            numeros_disponiveis=json.dumps(numeros_disponiveis),
                            numeros_sorteados=json.dumps(numeros_sorteados),
                            jogo_id=jogo_id)

                # Realização do sorteio
                # Verifica se o tipo da cartela é uma fração ou um número decimal
                if tipo_cartela == 'fracionarios':
                    # Converte a string de fração em uma fração do Python e depois para float
                    numero_sorteado = float(Fraction(numero_sorteado))
                else:
                    # Se a cartela é decimal, assume-se que o número sorteado já está em formato decimal.
                    numero_sorteado = str(decimal_para_fracao_irredutivel(numero_sorteado))

                # Retorna o número sorteado em formato JSON
                return jsonify({'numero_sorteado': numero_sorteado})
            else:
                return jsonify({'error': 'Não há mais números disponíveis para sortear.'})

        else:
            # Se não há informação do jogo, retorna uma mensagem de erro.
            return jsonify({'error': 'Informações do jogo não encontradas.'})

    # Se o método é GET, exibe a página de sorte com a lista de jogos.
    return render_template('sorteio.html', jogos=jogos)

if __name__ == '__main__':
    app.run()