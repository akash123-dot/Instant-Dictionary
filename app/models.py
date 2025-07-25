from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def defineuser(self):
        return f"User: {self.username}\nPassword: {self.password} "

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, mypassword):
        return check_password_hash(self.password, mypassword)
    
