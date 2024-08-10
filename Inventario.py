from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Cambia esto a una clave secreta segura

# Usuario y contraseña de ejemplo
USERS = {
    'user1': 'password123',
    'user2': 'password456',
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Verifica si el usuario y la contraseña son correctos
        if USERS.get(username) == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            # Solo pasa el error si la autenticación falla
            return render_template('login.html', error='Nombre de usuario o contraseña incorrectos')
    return render_template('login.html')


@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f'Hola, {session["user"]}! Bienvenido a la página de inicio.'

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
