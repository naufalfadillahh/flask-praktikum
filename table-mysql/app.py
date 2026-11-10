from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi koneksi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'        # Ganti dengan nama pengguna Anda
app.config['MYSQL_PASSWORD'] = ''         # Ganti dengan kata sandi Anda jika ada
app.config['MYSQL_DB'] = 'mahasiswadb'   # Nama database
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inisialisasi MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mahasiswa")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    npm = request.form['npm']
    kelas = request.form['kelas']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO mahasiswa (name, npm, kelas) VALUES (%s, %s, %s)", (name, npm, kelas))
    mysql.connection.commit()
    cur.close()

    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)