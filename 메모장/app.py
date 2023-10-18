from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = translator.translate(text, src='en', dest='ko').text
        return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
