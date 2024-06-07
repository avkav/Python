from flask import Flask, render_template

app = Flask(__name__)

@app.route("/peliculas")
def uso_diccionarios():
    lobo={
        "Nombre": "El lobo del Wall Street",
        "Año": "2013",
        "Protagonista": "Leonardo Di Caprio",
    }
    return render_template("dicionarios.html",destacada =lobo)


if __name__ == "__main__":
    app.run()
