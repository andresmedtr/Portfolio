from . import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(250), nullable=False)
    technologies_used = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.name,
            'url': self.name,
            'technologies_used': self.description
       }


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False)  # Profile name
    role = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text, nullable=False)  # Profile bio
    email = db.Column(db.String(100), nullable=False, unique=True)  # Profile email
    phone = db.Column(db.String(12))  # LinkedIn URL
    linkedin = db.Column(db.String(200))  # LinkedIn URL
    github = db.Column(db.String(200))  # GitHub URL

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'bio': self.bio,
            'email': self.email,
            'linkedin': self.linkedin,
            'github': self.github
        }