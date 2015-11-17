from flask import Flask, render_template, json, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
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
        query = """select votantes.doc_serie, votantes.doc_num from votantes
        where votantes.doc_serie = %s and votantes.doc_num = %s;"""
        cursor.execute(query, (serie, numero))
        return json.dumps(str(cursor.fetchall()))
    else:
        return json.dumps('false')


@app.route('/vote', methods=['POST', 'GET'])
def vote():
    if request.method == 'GET':
        return render_template('voting.html')
    else:
        try:
            cursor = mysql.connection.cursor()
            data = json.loads(request.data)
            candidato = data.get('candidato')
            if candidato:
                if candidato == 1:
                    query = """insert into votos(opcion_voto, observado) values(1,0)"""
                if candidato == 2:
                    query = """insert into votos(opcion_voto, observado) values(2,0)"""
            else:
                query = """insert into votos(opcion_voto, observado) values(null,0)"""
            cursor.execute(query)
        except Exception as error:
            print(error)
if __name__ == "__main__":
    app.run()
