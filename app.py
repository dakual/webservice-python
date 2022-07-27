from flask import Flask, render_template
from response import Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    response = Response("Hello Python! This is Python Flask rest api!")
    return response.get()

if __name__ == '__main__':
    app.run(debug=True)