from flask import Flask, request, render_template, make_response, send_file, jsonify, flash, redirect, session
from flask_session import Session
import random
from fractions import Fraction
from reportlab.pdfgen import canvas
from io import BytesIO
import json
from helpers import gerar_numero_fracionario, gerar_numero_decimal, gerar_numero_ambos, serialize_fraction
from werkzeug.security import generate_password_hash, check_password_hash
import os, secrets, string
from cs50 import SQL

app = Flask(__name__, static_folder="static")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///bingo.db")

SECRET_KEY = 'U7^GL4RuH$d^LWaHTAs9!O4Fu'
app.template_folder = 'templates'

CREATE_TABLE_PROFESSOR = """
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);


"""

def init_db():
    db.execute(CREATE_TABLE_PROFESSOR)
        # Adicione as outras tabelas aqui...

init_db()

numeros_disponiveis = [] # Lista de números para gerar as cartelas e realizar o sorteio
numeros_sorteados = [] # Declara a lista de números sorteados

# Verify if username already exists in bingo.db
def username_exists(email):
    existing_username = db.execute("SELECT email FROM professor WHERE email = :email", email=email)
    return len(existing_username) > 0

# INÍCIO
@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')

# REGISTRO, LOGIN E LOGOUT
@app.route("/register", methods=["GET", "POST"])
def registro():
    """Register user"""
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Verificar se o usuário digitou e-mail e senha
        if not email or not password:
            flash('Preencha todos os campos.')
            return render_template("register.html")  # Adicione essa linha

        # Verificar se o e-mail está disponível
        if username_exists(email):
            flash('E-mail já utilizado.')
            return render_template("register.html")  # Adicione essa linha

        # Inserir hash_password em bingo.db
        password_hash = generate_password_hash(password)

        # Insert hash_password into finance.db
        db.execute("INSERT INTO professor (email, password) VALUES (:email, :password_hash)", email=email, password_hash=password_hash)  # Corrija o parâmetro

        # Logar o usuário depois de cadastro com sucesso
        rows = db.execute("SELECT * FROM professor WHERE email = ?", email)
        session["user_id"] = rows[0]["id"]
        return redirect("/gerar_cartelas")

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Garantir que o usuário inseriu e-mail
        if not request.form.get("email"):
            flash('Insira um e-mail', 'error')
            return render_template("login.html")

        # Garantir que o usuário inseriu a senha
        elif not request.form.get("password"):
            flash('Insira a senha', 'error')
            return render_template("login.html")

        rows = db.execute("SELECT * FROM professor WHERE email = ?", request.form.get("email"))

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
        return redirect("/gerar_cartelas")


    else:
        # User reached route via GET (as by clicking a link or via redirect)
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Esquecer qualquer usuário
    session.clear()

    # Redirecionar para a página inicial
    return redirect("/")

#GERAÇÃO DE CARTELAS
@app.route('/geracao', methods=['GET', 'POST'])
def gerar_cartelas():
    global numeros_disponiveis

    cartelas = []

    if request.method == 'POST':
        num_cartelas = int(request.form.get('numCartelas'))
        tipo_cartelas = request.form.get('tipoCartelas')

        # Gere 74 números com base na escolha do usuário apenas se a lista estiver vazia
        if not numeros_disponiveis:
            if tipo_cartelas == "fracionarios":
                numeros_disponiveis = [gerar_numero_fracionario() for _ in range(74)]
            elif tipo_cartelas == "decimais":
                numeros_disponiveis = [gerar_numero_decimal() for _ in range(74)]
            else:  # Ambos
                for _ in range(74):
                    escolha = random.choice(["fracionario", "decimal"])
                    if escolha == "fracionario":
                        numeros_disponiveis.append(gerar_numero_fracionario())
                    else:
                        numeros_disponiveis.append(gerar_numero_decimal())

        for _ in range(num_cartelas):
            cartela = []

            numeros_unicos = random.sample(numeros_disponiveis, 24)  # Escolhe 24 números únicos

            for numero in numeros_unicos:
                cartela.append(numero)

            cartela.insert(12, "FREE")
            cartela = [cartela[i:i + 5] for i in range(0, len(cartela), 5)]
            cartelas.append(cartela)

        return render_template('cartelas.html', cartelas=cartelas)

    return render_template('geracao.html', cartelas=None)

@app.route('/cartelas', methods=['GET'])
def exibir_cartelas():
    return render_template('cartelas.html', cartelas=None)

#IMPRESSÃO DAS CARTELAS GERADAS
@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    cartelas = json.loads(request.form['cartelas'])  # Recupera as cartelas dos dados do formulário

    # Crie um buffer de bytes para armazenar o PDF
    buffer = BytesIO()

    # Inicialize o objeto Canvas do ReportLab
    c = canvas.Canvas(buffer)
    c.setPageSize((595, 842))  # Tamanho A4

    # Defina as dimensões iniciais e o espaçamento
    x_init, y_init = 50, 820  # Ajustado y_init para evitar sobreposição
    offset_coluna = 260  # Deslocamento entre colunas
    offset_linha = 250  # Deslocamento entre linhas
    tamanho_celula = 40  # Tamanho das células
    espaco_extra = 10  # Espaço extra para separação das linhas de cartelas

    coluna_count, linha_count = 0, 0

    for idx, cartela in enumerate(cartelas):
        x, y = x_init + coluna_count * offset_coluna, y_init - linha_count * (offset_linha + espaco_extra)

        # Desenha a borda externa da cartela englobando nome e número
        c.rect(x, y - (5 * tamanho_celula + 30), 5 * tamanho_celula, 5 * tamanho_celula + 30)  # Ajustado para +35

        # Desenha a grade da cartela
        for i in range(6):  # Adicionado +1 para desenhar a borda inferior
            c.line(x, y - i * tamanho_celula - 30, x + 5 * tamanho_celula, y - i * tamanho_celula - 30)  # Ajustado para -30
        for j in range(6):
            c.line(x + j * tamanho_celula, y - 30, x + j * tamanho_celula, y - 5 * tamanho_celula - 30)  # Ajustado para -30

        # Escreve os números na cartela
        for i, linha in enumerate(cartela):
            x_temp = x
            for j, numero in enumerate(linha):
                c.drawCentredString(x_temp + tamanho_celula / 2, y - (i * tamanho_celula + tamanho_celula / 2 + 6) - 30, str(numero))
                x_temp += tamanho_celula

        # Adicione o número da cartela no canto superior direito
        c.drawRightString(x + 5 * tamanho_celula - 5, y - 22, f"#{idx + 1}")  # Ajustado para -15

        # Adicione um espaço no canto superior esquerdo para o nome
        c.drawString(x + 5, y - 23, "Nome: _____________")  # Ajustado para -15

        coluna_count += 1
        if coluna_count > 1:  # Se tivermos completado 2 colunas, vá para a próxima linha
            coluna_count = 0
            linha_count += 1
            if linha_count > 2:  # Se tivermos completado 3 linhas, comece uma nova página
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
    tipo_sorteio = None  # Inicializa o tipo de sorteio

    if request.method == 'POST':
        tipo_sorteio = request.form.get('tipoSorteio')

    return render_template('sorteio.html', tipo_sorteio=tipo_sorteio)

@app.route('/sorteio/realizar', methods=['POST'])
def realizar_sorteio():
    tipo_sorteio = request.form.get('tipoSorteio')

    if not numeros_disponiveis:
        return jsonify({'numero_sorteado': None})

    numero_sorteado = None

    if tipo_sorteio == "fracionarios":
        numero_sorteado = random.choice([n for n in numeros_disponiveis if isinstance(n, Fraction)])
    elif tipo_sorteio == "decimais":
        numero_sorteado = random.choice([n for n in numeros_disponiveis if isinstance(n, float)])
    else:
        numero_sorteado = random.choice(numeros_disponiveis)

    if numero_sorteado:
        numeros_sorteados.append(numero_sorteado)
        numeros_disponiveis.remove(numero_sorteado)
        numero_sorteado_float = float(numero_sorteado)
    else:
        numero_sorteado_float = None

    return jsonify({'numero_sorteado': numero_sorteado_float})

if __name__ == '__main__':
    app.run(debug=True)
