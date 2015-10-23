from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()

@app.route('/login',methods=['POST'])
def signUp():


    _serie = request.form['credSerie']
    _numero = request.form['credNumero']


    # validate the received values
    if _serie and _numero:
        return json.dumps({'html':'<span>Usuario valido</span>'})
    else:
        return json.dumps({'html':'<span>Ingrese los valores en los campos requeridos, por favor</span>'})
