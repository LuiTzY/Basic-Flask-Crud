from flask import Flask,render_template,redirect,url_for,request,flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key  = "CRUD_CON_FLASK"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flask_crud'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    return render_template('index.html',data=contactos)

@app.route('/crear-contacto',methods=['POST'])
def crear_contacto():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        
        cursor = mysql.connection.cursor()
        cursor.execute("insert into contactos values(null,%s,%s,%s)",(nombre,apellidos,email))
        cursor.connection.commit()
        flash("Contacto creado exitosamente")
        return redirect(url_for('index'))
    
@app.route("/eliminar-contacto/<string:id>")
def eliminar_contacto(id):
    if id is not None:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM contactos WHERE id = %s",(id))
        cursor.connection.commit()
        flash(f"Se ha eliminado correctamente el usuario con id: {id}")
        return redirect(url_for('index'))
    else:
        flash("Debe de proporcionar un id para eliminar un usuario")
        
@app.route("/editar/<id>")
def editar_contacto(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contactos WHERE id = %s",id)
    contacto = cursor.fetchall()
    return render_template('editar.html',contacto=contacto[0])
        
@app.route("/actualizar-contacto/<string:id>",methods=["POST"])       
def actualizar_contacto(id):
    if id is not None:
        if request.method == "POST":
            cursor = mysql.connection.cursor()
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            email = request.form['email']
            cursor.execute("UPDATE contactos SET nombre=%s,apellido=%s,email=%s  WHERE id = %s",(nombre,apellidos,email,id))
            cursor.connection.commit()
            flash(f"Se ha actualizado correctamente el usuario con id: {id}")
            return redirect(url_for('index'))
        else:
            flash("Debe de proporcionar un id para actualizar un usuario")
        
if __name__ == "__main__":
    app.run(debug=True,port=3000)