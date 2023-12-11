# /app/models.py

from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)

    def set_password(self, password):
        print(password)
        self.password_hash = generate_password_hash(password)
        print(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)
    

#############################################################

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)

class RelationshipUserJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_job = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_relationship_user_job = db.Column(db.Integer, db.ForeignKey('relationship_user_job.id'), nullable=False)
    description = db.Column(db.String(255))
    date_create = db.Column(db.Date)
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    id_assessment = db.Column(db.Integer, db.ForeignKey('assessment.id'))
    state = db.Column(db.Enum('Pending', 'InProgress', 'Completed'))

class JobDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_relationship_user_job = db.Column(db.Integer, db.ForeignKey('relationship_user_job.id'), nullable=False)
    description = db.Column(db.String(255))
    day = db.Column(db.Time)
    time = db.Column(db.Time)

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_service = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    assessment_user_client = db.Column(db.Float)
    comment_user_client = db.Column(db.String(255))
    assessment_user_provider = db.Column(db.Float)
    comment_user_provider = db.Column(db.String(255))
    state = db.Column(db.Enum('Pending', 'Approved', 'Rejected'))