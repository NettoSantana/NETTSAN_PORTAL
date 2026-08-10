# CAMINHO COMPLETO: C:\Users\vlula\OneDrive\Área de Trabalho\Projetos Backup\NETTSAN_PORTAL\app.py
# DATA E HORA DO ULTIMO RECODE: 2026-08-10 11:10 -03:00
# MOTIVO DA ALTERACAO: Criar a aplicacao Flask inicial do portal comercial da NettSan e disponibilizar as paginas publicas principais.

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/gestflow")
def gestflow():
    return render_template("gestflow.html")


@app.get("/indflow")
def indflow():
    return render_template("indflow.html")


@app.get("/nr12")
def nr12():
    return render_template("nr12.html")


@app.get("/cases")
def cases():
    return render_template("cases.html")


@app.get("/sobre")
def sobre():
    return render_template("sobre.html")


@app.get("/contato")
def contato():
    return render_template("contato.html")


@app.get("/health")
def health():
    return {"status": "ok"}, 200


@app.errorhandler(404)
def pagina_nao_encontrada(_erro):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
