from flask import jsonify, request, Blueprint
from .models import Profile, Project, db

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def hello():
    return jsonify("This is a message from the backend showing it's working")

@api.route('/projects', methods=['GET'])
def get_projects(): 
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@api.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    name=data.get('name')
    description= data.get('description')
    url=data.get('url')
    technologies_used=data.get('technologies_used')
    
    if not name or not description:
        return jsonify({"Error": 'Missing information'}), 400
    project = Project(name=name, description=description, url=url, technologies_used=technologies_used)
    db.session.add(project)
    db.session.commit()
    return jsonify({'Project added':project.to_dict()}), 201

@api.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profile = Profile.query.get(profile_id)
    if profile:
        return jsonify(profile.to_dict())
    else:
        return jsonify('Profile not found'), 404
    

@api.route('/profile/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.json
    profile = Profile.query.get(profile_id)
    if profile:
        profile.name = data['name']
        profile.bio = data['bio']
        profile.email = data['email']
        profile.role = data['role']
        profile.phone = data.get('phone', profile.phone)
        profile.linkedin = data.get('linkedin', profile.linkedin)
        profile.github = data.get('github', profile.github)
        db.session.commit()
        return jsonify(profile.to_dict())
    return jsonify('Profile not found'), 404
