from flask import Blueprint,request,jsonify
from flask.views import MethodView
from app.utils.jwt_helper import generate_token
from app.models import User
from app import db


auth_bp = Blueprint('auth', __name__)

class SignUpView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 409

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
       
class LoginView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        token = generate_token(user.id)
        
        return jsonify({'token': token}), 200
    



auth_bp.add_url_rule('/signup', view_func=SignUpView.as_view('signup'))
auth_bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
