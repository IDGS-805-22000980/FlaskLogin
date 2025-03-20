from models import db, Usuarios
from app import app 


with app.app_context():
    nuevo_usuario = Usuarios(
        email="usuario@example.com",
        fullName="Luis Eduardo Silva Aguirre"
    )
    nuevo_usuario.set_password("123456")  

    db.session.add(nuevo_usuario)  
    db.session.commit()  

    print("Usuario creado con éxito")
