# /app/models.py

from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True) 

    def set_password(self, password):
        print(password)
        self.password_hash = generate_password_hash(password)
        print(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)
       

#############################################################
import datetime 
from flask_sqlalchemy import SQLAlchemy

class Service(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_relationship_user_job = db.Column(db.Integer, db.ForeignKey('relationship_user_job.id', use_alter=True), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date_create = db.Column(db.Date, default=datetime, nullable=False)
    date_start = db.Column(db.Date, default=datetime, nullable=False)
    date_end = db.Column(db.Date, default=datetime, nullable=False)
    attention_time = db.Column(db.Date, default=datetime, nullable=False)
    id_assessment = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    state = db.Column(db.Enum('pending', 'in_progress', 'completed'), nullable=False)
    
    def _repr_(self):
        return f"<Service {self.description}>"
    

class Relationship_user_job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_job = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    def __repr__(self):
        return f"<Relationship_user_job {self.id}>"


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Job {self.description}>"
    

class Job_detail(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    id_relationship_user_job = db.Column(db.Integer, db.ForeignKey('relationship_user_job.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    attention_day = db.Column(db.Date, default=datetime, nullable=False)
    attention_time = db.Column(db.Date, default=datetime, nullable=False)
    
    
    def _repr_(self):
        return f"<Job_detail {self.id}>"    

class Assessment(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    id_service = db.Column(db.Integer, db.ForeignKey('service.id', use_alter=True), nullable=False)
    assessment_user_client = db.Column(db.Float, nullable=False)
    comment_user_client = db.Column(db.Float, nullable=False)
    assessment_user_provider = db.Column(db.Float, nullable=False)
    comment_user_provier = db.Column(db.Float, nullable=False)
    state = db.Column(db.Enum('canceled', 'evaluate', 'aproved'), default='aproved', nullable=False)
    
    def _repr_(self):
        return f"<Assessment {self.id}>"    