from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuarios(db.Model, UserMixin):
    __tablename__ = 'Usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False)  
    fullName = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        """Guarda la contraseña encriptada."""
        self.contrasenia = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña encriptada."""
        return check_password_hash(self.contrasenia, password)

    def get_id(self):
        """Devuelve el identificador único del usuario."""
        return str(self.idUsuario)
