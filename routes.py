from app import *

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/quem-somos", methods=["GET", "POST"])
def quemSomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        userDetails = request.form
        emailUsuario = userDetails["email"]
        assuntoMensagem = userDetails["assunto"]
        mensagemUsuario = userDetails["descricao"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mensagem(email, assunto, descricao) VALUES(%s, %s, %s)", (emailUsuario, assuntoMensagem, mensagemUsuario))
        cur.connection.commit()
        cur.close()
        flash("Mensagem registrada com sucesso!")
    return render_template("contato.html")

@app.route("/dados-listados", methods=["GET", "POST"])
def dadosListados():
    cur = mysql.connection.cursor()
    cur.execute("SELECT email, assunto, descricao from mensagem")
    email = []
    assunto = []
    mensagem = []
    for i in cur:
        email.append(i[0])
        assunto.append(i[1])
        mensagem.append(i[2])
    
    colunas = ("Email", "Assunto", "Mensagem")
    dados = list(zip(email, assunto, mensagem))
    return render_template("mensagens.html", colunas = colunas, dados = dados)