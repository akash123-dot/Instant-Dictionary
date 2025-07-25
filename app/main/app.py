from flask import Blueprint, render_template, request
from flask.views import MethodView
from app.dictionary.dictionary_logic import Dictionary


main_app = Blueprint("main", __name__, template_folder='templates')


class HomePage(MethodView):
    def get(self):
        return render_template('home.html')
    
class AboutPage(MethodView):
    def get(self):
        return render_template('about.html')
    
class DictionaryPage(MethodView):
    def get(self):
        return render_template('dictionary.html')
    
    def post(self):
        term = request.form.get('term')
        definition = Dictionary(term)
        data_list = definition.GetData()
        return render_template('dictionary.html', data=data_list)

class APIPage(MethodView):
    def get(self):
        return render_template('api_view.html')

main_app.add_url_rule('/', view_func=HomePage.as_view('homepage'))
main_app.add_url_rule('/about', view_func=AboutPage.as_view('aboutpage'))
main_app.add_url_rule('/dictionary', view_func=DictionaryPage.as_view('dictionarypage'))
main_app.add_url_rule('/apiview', view_func=APIPage.as_view('apipageview'))

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)