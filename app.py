from flask import Flask,render_template, request, json, redirect,session
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'secreto'
#MySQL Configuracion
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin_1572003_jesc'
app.config['MYSQL_DATABASE_DB'] = 'tienda_lentes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('wikifc_bt.html')

@app.route('/addProduct', methods=['POST'])
def AddProduct():
    if session.get('user'):
        _id_producto = request.form['inputIdProducto']
        _marca = request.form['inputMarca']
        _modelo = request.form['inputModelo']
        _color = request.form['inputColor']
        _descripcion = request.form['inputDescription']
        _precio = request.form['inputPrecio']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('crearProducto', (_id_producto, _marca, _modelo, _color, _descripcion, _precio,))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect('adminHome')
        else:
            return render_template('error.html', error='Un error detectado')

    else:
        return render_template('error.html', error='Acceso no Autorizado')
    cursor.close
    conn.close