# /auth/views.py
from flask import request, jsonify
from . import auth
from ..models import User, db

@auth.route("/api/register", methods=['POST'])
def register():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not password:
        return jsonify({'message': 'Datos incompletos'}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({'message': 'El correo electrónico ya existe'}), 400

    new_user = User(email=email, first_name=first_name, last_name=last_name)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201


@auth.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        # Tu lógica de inicio de sesión aquí
        return jsonify({'message': 'Inicio de sesión exitoso', 'user_id': user.id, 'email': user.email}), 200
    else:
        return jsonify({'message': 'Correo electrónico o contraseña inválidos'}), 401




@auth.route("/")
def index():
    return jsonify({'users': "hola"})



# /auth/views.py
from flask import request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User


@auth.route("/api/logout")
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Cierre de sesión exitoso'}), 200



@auth.route("/api/user_info")
@login_required
def user_info():
    # Accede a la información del usuario actualmente autenticado
    user_info = {
        'user_id': current_user.id,
        'email': current_user.email,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'location': current_user.location,
    }
    return jsonify(user_info), 200