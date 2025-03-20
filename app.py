from flask import Flask, redirect, request, url_for, render_template, flash
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Usuarios
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import LoginForm

app = Flask(__name__) 
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
db.init_app(app)


login_manager = LoginManager()  
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form) 
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        
        user = Usuarios.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso. bienvenido', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Los datos son incorrectos', 'danger')

    return render_template('login.html', form=form)

@app.route('/inicio')
@login_required
def inicio():
    return render_template('inicio.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
