from flask import Blueprint, jsonify, request
from flask.views import MethodView
from app.utils.jwt_helper import Checkauth
from app.dictionary.dictionary_logic import Dictionary

api_bp = Blueprint('api', __name__)

class FetchResultView(MethodView):
    def post(self):
        token = request.headers.get('Authorization')
        user_id = Checkauth(token)
        if user_id == None:
            return jsonify({'error': 'Unauthorized'}), 401
        
        data = request.get_json()
        word = data.get('word')
        if not word:
            return jsonify({'error': 'Word is required'}), 400
        
        dictionary = Dictionary(word)
        result = dictionary.GetData()
        return jsonify({'word': word, 'definitions': result}), 200
    

api_bp.add_url_rule('/fetch_result', view_func=FetchResultView.as_view('fetch_result'))