from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/ssrf')
def ssrf():
    url = request.args.get('url')
    return requests.get(url).text

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save('/tmp/' + f.filename)
    return "Uploaded"

@app.route('/eval')
def insecure(): return eval(request.args.get('input'))
