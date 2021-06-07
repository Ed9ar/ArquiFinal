from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'comicwire_admin'
app.config['MYSQL_PASSWORD'] = 'AdminPassComicwire1234'
app.config['MYSQL_DB'] = 'users_twitters'

mysql = MySQL(app)

@app.route("/")
def UsuarioService():

    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM users")
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('UsuarioService.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

