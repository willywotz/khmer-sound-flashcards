from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route('/speak', methods=['GET'])
def speak():
    text = request.args.get('text')

    if not text:
        return {"error": "No text provided"}, 400

    try:
        return send_file('assets/consonants/'+text+'.mp3')
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
