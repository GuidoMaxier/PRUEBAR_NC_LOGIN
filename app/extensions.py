# /app/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_cors import CORS  # Importa la extensión CORS

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
login_manager = LoginManager()

cors = CORS()  # Inicializa la extensión CORS


# Configuración CORS
def configure_cors(app):
    cors.init_app(app, origins="*")  # Configura los orígenes permitidos.


