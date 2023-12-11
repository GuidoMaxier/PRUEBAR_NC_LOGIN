# /auth/views.py

from flask import request, jsonify
from . import auth
from ..models import User, db

# @auth.route("/api/register", methods=['POST'])
# def register():
#     data = request.get_json()

#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if not username or not email or not password:
#         return jsonify({'message': 'Incomplete data'}), 400

#     existing_user = User.query.filter_by(username=username).first()

#     if existing_user:
#         return jsonify({'message': 'Username already exists'}), 400

#     new_user = User(username=username, email=email)
#     new_user.set_password(password)

#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'User registered successfully'}), 201


@auth.route("/api/register", methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    print(password)

    if not username or not email or not password:
        return jsonify({'message': 'Incomplete data'}), 400

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# /auth/views.py
from flask import request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User

@auth.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


# /auth/views.py
from flask import jsonify
from flask_login import login_required
from . import auth
from ..models import User

@auth.route("/api/users")
@login_required
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({'username': user.username, 'email': user.email})
    return jsonify({'users': user_list})



@auth.route("/")
def index():
    return jsonify({'users': "hola"})
