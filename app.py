# CAMINHO COMPLETO: C:\Users\vlula\OneDrive\Área de Trabalho\Projetos Backup\NETTSAN_PORTAL\app.py
# DATA E HORA DO ULTIMO RECODE: 2026-11-25 08:51 -03:00
# MOTIVO DA ALTERACAO: Adicionar a rota de Automacao Industrial e preservar a pagina NR12 como subarea de seguranca de maquinas.

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/automacao-industrial")
def automacao_industrial():
    return render_template("automacao_industrial.html")


@app.get("/nr12")
def nr12():
    return render_template("nr12.html")


@app.get("/indflow")
def indflow():
    return render_template("indflow.html")


@app.get("/gestflow")
def gestflow():
    return render_template("gestflow.html")


@app.get("/automacao-residencial")
def automacao_residencial():
    return render_template("automacao_residencial.html")


@app.get("/eletrica-residencial")
def eletrica_residencial():
    return render_template("eletrica_residencial.html")


@app.get("/solucoes-sob-medida")
def solucoes_sob_medida():
    return render_template("solucoes_sob_medida.html")


@app.get("/cases")
def cases():
    return redirect(f"{url_for('nr12')}#cases", code=301)


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
