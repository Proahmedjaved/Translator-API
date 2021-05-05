from flask import Flask, request
from translate import translate

app = Flask(__name__)

@app.route('/english_to_french', methods=['POST'])
def en_to_fr():
    try:
        return translate(request.form['text'], 'en','fr')
    except Exception as e:
        print('Something went wrong!', str(e))

@app.route('/german_to_french', methods=['POST'])
def de_to_fr():
    try:
        return translate(request.form['text'], 'de', 'fr')
    except Exception as e:
        print('Something went wrong!', str(e))

@app.route('/spanish_to_french', methods=['POST'])
def home():
    try:
        return translate(request.form['text'], 'es', 'fr')
    except Exception as e:
        print('Something went wrong!', str(e)) 


if __name__ == '__main__':
    app.run()