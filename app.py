from flask import Flask, request, jsonify, Response, render_template
from translate import translate
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/english_to_french', methods=['POST'])
def en_to_fr():
    try:
        return Response(
            json.dumps(translate(request.form['text'], 'en','fr')),
            mimetype='application/json'
        )
    except Exception as e:
        print('Something went wrong!', str(e))

@app.route('/german_to_french', methods=['POST'])
def de_to_fr():
    try:
        return Response(
            json.dumps(translate(request.form['text'], 'de', 'fr')),
            mimetype='application/json'
        )
    except Exception as e:
        print('Something went wrong!', str(e))

@app.route('/spanish_to_french', methods=['POST'])
def es_to_fr():
    try:
        return Response(
            json.dumps(translate(request.form['text'], 'es', 'fr')),
            mimetype='application/json'
        )
    except Exception as e:
        print('Something went wrong!', str(e)) 


if __name__ == '__main__':
    app.run()