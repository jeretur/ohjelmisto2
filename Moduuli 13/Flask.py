from flask import Flask, request

app = Flask(__name__)


@app.route('/alkuluku/<numero>')
def alkuluku(numero):
    luku = int(numero)

    if luku == 1 or luku == 0:
        print('Annettu luku on alkuluku.')
    elif luku < 0:
        print('Annettu luku ei ole alkuluku.')

    else:
        onkoAlku = False
        for i in range(2, luku):
            if luku % i == 0:
                onkoAlku = True

        if onkoAlku:
            print('Annettu luku ei ole alkuluku')
        else:
            print('Annettu luku on alkuluku')
        vastaus = {
            "Number": luku,
            "isPrime": onkoAlku
        }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
