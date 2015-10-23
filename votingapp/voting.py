from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()

@app.route('/login',methods=['POST'])
def signUp():

    # read the posted values from the UI
    _serie = request.form['inputName']
    _numero = request.form['inputEmail']


    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
