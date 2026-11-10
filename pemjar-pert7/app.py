from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'rahasia-tebakan-nyawa'

@app.route('/')
def index():
    # Inisialisasi angka acak dan sistem 5 nyawa saat pertama kali membuka game
    if 'angka' not in session:
        session['angka'] = random.randint(1, 100)
        session['nyawa'] = 5
    return render_template('index.html', pesan=None, status=None)

@app.route('/tebak', methods=['POST'])
def tebak():
    if 'angka' not in session:
        return redirect(url_for('index'))

    tebakan = int(request.form['tebakan'])
    angka = session.get('angka')
    
    # Setiap tebakan masuk, nyawa langsung berkurang 1
    session['nyawa'] -= 1
    nyawa_sisa = session['nyawa']
    
    pesan = ""
    status = ""  # Variabel penanda untuk dioper ke CSS

    if tebakan == angka:
        pesan = f'Selamat! Anda berhasil menebak angka {angka} dengan tepat! 🎉'
        status = "menang"
    elif nyawa_sisa <= 0:
        pesan = f'Game Over! Kesempatan Anda habis. Angka yang benar adalah {angka}. 😢'
        status = "kalah"
    else:
        status = "salah"
        if tebakan < angka:
            pesan = f'Tebakan Anda terlalu rendah. (Sisa Nyawa: {nyawa_sisa}) 👇'
        else:
            pesan = f'Tebakan Anda terlalu tinggi. (Sisa Nyawa: {nyawa_sisa}) 👆'

    return render_template('index.html', pesan=pesan, status=status)

@app.route('/reset')
def reset():
    # Hapus semua session data game untuk mengulang kembali
    session.pop('angka', None)
    session.pop('nyawa', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)