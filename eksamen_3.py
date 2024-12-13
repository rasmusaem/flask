from flask import Flask, render_template, request, redirect, url_for, flash, session
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
app.secret_key = 'din_secret_key'  # Nødvendig for session og flash

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/data_visning')
def data_visning():
    if 'user' not in session:
        flash('Du skal være logget ind for at få adgang.', 'danger')
        return redirect(url_for('login'))
    return render_template('data_visning.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # hardkodet brugervalidering
        if username == 'lasse' and password == 'frank':
            session['user'] = username  # Gem bruger i session
            flash('Du er logget ind!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Forkert brugernavn eller adgangskode', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Du er logget ud.', 'info')
    return redirect(url_for('login'))

@app.route('/protected_page')
def protected_page():
    if 'user' not in session:
        flash('Du skal være logget ind for at få adgang.', 'danger')
        return redirect(url_for('login'))
    return render_template('protected_page.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
