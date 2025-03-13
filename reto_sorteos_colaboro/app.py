import os
import sqlite3
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
import qrcode

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cámbiala por una clave segura

DATABASE = 'submissions.db'
QR_FOLDER = os.path.join('static', 'qr_codes')
if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            number TEXT NOT NULL,
            state TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            qr_code_filename TEXT NOT NULL,
            qr_content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Diccionario de colaboradores (correo: contraseña)
collaborators = {
    'colaborador@example.com': 'password1',
    'otrocolaborador@example.com': 'password2'
}

# Página de selección de rol
@app.route('/')
def choose_role():
    return render_template('choose_role.html')

# ------------------------
# Flujo Comprador
# ------------------------
@app.route('/buyer', methods=['GET', 'POST'])
def buyer():
    if request.method == 'POST':
        qr_content = request.form.get('qr_content')
        if not qr_content:
            flash("Por favor, ingresa o escanea el contenido del QR.")
            return redirect(url_for('buyer'))
        # Buscar el registro en la base de datos
        conn = get_db_connection()
        submission = conn.execute('SELECT * FROM submissions WHERE qr_content = ?', (qr_content,)).fetchone()
        conn.close()
        if submission:
            return render_template('buyer_result.html', submission=submission)
        else:
            flash("No se encontró información para el QR ingresado.")
            return redirect(url_for('buyer'))
    return render_template('buyer.html')

# ------------------------
# Flujo Colaborador
# ------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in collaborators and collaborators[email] == password:
            session['logged_in'] = True
            session['collaborator_email'] = email
            return redirect(url_for('collaborator_form'))
        else:
            flash('Correo o contraseña incorrecta.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Formulario para ingreso de datos (solo para colaboradores autenticados)
@app.route('/collaborator_form', methods=['GET'])
def collaborator_form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('collaborator_form.html')

@app.route('/submit_collaborator', methods=['POST'])
def submit_collaborator():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    name = request.form.get('name')
    email = request.form.get('email')
    number = request.form.get('number')
    state = request.form.get('state')
    if not all([name, email, number, state]):
        flash('Por favor, llena todos los campos.')
        return redirect(url_for('collaborator_form'))
    
    # Generar identificador único y contenido del QR
    unique_id = str(uuid.uuid4())
    qr_content = f"SorteosTec-{unique_id}"
    qr_img = qrcode.make(qr_content)
    qr_filename = f"{unique_id}.png"
    qr_path = os.path.join(QR_FOLDER, qr_filename)
    qr_img.save(qr_path)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO submissions (name, email, number, state, timestamp, qr_code_filename, qr_content) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (name, email, number, state, timestamp, qr_filename, qr_content)
    )
    conn.commit()
    conn.close()

    return render_template('submission_success.html', qr_filename=qr_filename, qr_content=qr_content)

# Dashboard para colaboradores: muestra los datos registrados en una tabla
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    conn = get_db_connection()
    submissions = conn.execute('SELECT * FROM submissions ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', submissions=submissions)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('choose_role'))

if __name__ == '__main__':
    app.run(debug=True)
