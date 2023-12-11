# app/views.py

from flask import Blueprint
from flask_restful import Api, Resource
from flask import request, jsonify
from .models import db, User, Job, Relationship_user_job

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({'user': user.to_dict()})

    def post(self):
        data = request.get_json()
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.update(data)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})

class JobResource(Resource):
    def get(self, job_id):
        job = Job.query.get_or_404(job_id)
        return jsonify({'job': job.to_dict()})

    def post(self):
        data = request.get_json()
        new_job = Job(**data)
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job created successfully'}), 201

    def put(self, job_id):
        job = Job.query.get_or_404(job_id)
        data = request.get_json()
        job.update(data)
        db.session.commit()
        return jsonify({'message': 'Job updated successfully'})

    def delete(self, job_id):
        job = Job.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        return jsonify({'message': 'Job deleted successfully'})

class Relationship_user_jobResource(Resource):
    def get(self, relationship_id):
        relationship = Relationship_user_job.query.get_or_404(relationship_id)
        return jsonify({'relationship': relationship.to_dict()})

    def post(self):
        data = request.get_json()
        new_relationship = Relationship_user_job(**data)
        db.session.add(new_relationship)
        db.session.commit()
        return jsonify({'message': 'Relationship created successfully'}), 201

    def put(self, relationship_id):
        relationship = Relationship_user_job.query.get_or_404(relationship_id)
        data = request.get_json()
        relationship.update(data)
        db.session.commit()
        return jsonify({'message': 'Relationship updated successfully'})

    def delete(self, relationship_id):
        relationship = Relationship_user_job.query.get_or_404(relationship_id)
        db.session.delete(relationship)
        db.session.commit()
        return jsonify({'message': 'Relationship deleted successfully'})
    

# vistas para cada recurso
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(JobResource, '/jobs/<int:job_id>')
api.add_resource(Relationship_user_jobResource, '/relationships/<int:relationship_id>')
