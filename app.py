from flask import Flask, request
import os

app = Flask(__name__)

# Vulnerable to command injection
@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    return os.popen(cmd).read()

# Vulnerable to open redirect
@app.route('/redirect')
def redirect():
    target = request.args.get('url')
    return f'<meta http-equiv="refresh" content="0; url={target}">'
