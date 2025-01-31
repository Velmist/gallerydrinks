from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User, Bebida, Comentario
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
    bebidas = Bebida.query.all()
    return render_template('index.html', bebidas=bebidas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtén los datos del formulario
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Verifica que todos los campos estén presentes
        if not username or not email or not password or not confirm_password:
            flash('Todos los campos son obligatorios', 'danger')
            return redirect(url_for('register'))

        # Verifica que las contraseñas coincidan
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('register'))

        # Verifica si el usuario o el correo ya existen
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_user:
            flash('El nombre de usuario ya está en uso', 'danger')
            return redirect(url_for('register'))
        if existing_email:
            flash('El correo electrónico ya está en uso', 'danger')
            return redirect(url_for('register'))

        # Crea un nuevo usuario
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Por favor, inicia sesión.', 'success')
        return redirect(url_for('login'))

    # Si el método es GET, muestra el formulario de registro
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/bebida/<int:id>', methods=['GET', 'POST'])
def bebida_detail(id):
    bebida = Bebida.query.get_or_404(id)
    if request.method == 'POST':
        if current_user.is_authenticated:
            contenido = request.form['comentario']
            comentario = Comentario(contenido=contenido, user_id=current_user.id, bebida_id=bebida.id)
            db.session.add(comentario)
            db.session.commit()
            return redirect(url_for('bebida_detail', id=bebida.id))
        else:
            return redirect(url_for('login'))
    return render_template('detail.html', bebida=bebida)      
