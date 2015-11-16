from flask import Flask, render_template, json, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'votacionesDB'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def sign_up():
    cursor = mysql.connection.cursor()
    data = json.loads(request.data)
    serie = data.get('serie')
    numero = data.get('numero')
    # # validate the received values
    if serie and numero:
        cursor.execute("""select votantes.doc_serie, votantes.doc_num from votantes
        where votantes.doc_serie = %sserie and votantes.doc_num = %snumero;""", (serie, numero))
        print(cursor.fetchall())
        return json.dumps(str(cursor.fetchall()))
    else:
        return json.dumps('false')


if __name__ == "__main__":
    app.run()