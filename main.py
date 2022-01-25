import flask

app = flask.Flask(__name__)

@app.route('/procesar')
def procesar():
    print("se recibio la imagen")
    return "la imagen procesada"

if  __name__ == '__main__':
    app.run(host='0.0.0.0',port=80) 