from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'comicwire_admin'
app.config['MYSQL_PASSWORD'] = 'AdminPassComicwire1234'
app.config['MYSQL_DB'] = 'users_twitters'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def UsuarioService():

    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM users")
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    
    return render_template('UsuarioService.html', data=data)

@app.route("/twitter", methods=['GET', 'POST'])
def TwitterService():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        username = request.form.get("username")
        # getting input with name = lname in HTML form 
        twitter = username
        
    print(request.form.get("username"))
    return render_template('TwitterService.html', twitter=twitter)



@app.route("/csv", methods=['GET', 'POST'])
def CSVService():
   
    return UsuarioService()


if __name__ == '__main__':
    app.run(debug=True)

