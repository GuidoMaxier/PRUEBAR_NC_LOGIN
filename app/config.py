# /app/config.py

class Config:
    SQLALCHEMY_DATABASE_URI222222 = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root@localhost:3306/arreglos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
