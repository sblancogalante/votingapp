from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def sign_up():
    data = json.loads(request.data)
    serie = data.get('serie')
    numero = data.get('numero')
    # # validate the received values
    if serie and numero:
        return json.dumps('true')
    else:
        return json.dumps('false')


if __name__ == "__main__":
    app.run()
