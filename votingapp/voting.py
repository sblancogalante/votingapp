from flask import Flask, render_template, json, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'votacionesDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

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
        conn.commit()
        return json.dumps('true')
    else:
        return json.dumps('false')


if __name__ == "__main__":
    app.run()
