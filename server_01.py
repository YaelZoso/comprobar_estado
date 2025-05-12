from flask import Flask

app = Flask(__name__)


cuenta = 0


@app.route("/")
def confirmacion():
    global cuenta
    cuenta += 1
    return f"Hola mundo {cuenta}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
