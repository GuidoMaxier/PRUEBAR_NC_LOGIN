# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db, migrate, ma, login_manager, configure_cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    login_manager.init_app(app)

    # Configuración CORS
    configure_cors(app)


    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    with app.app_context():
        from .auth import auth
        app.register_blueprint(auth)

        return app
