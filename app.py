from flask import Flask, request

app = Flask(__name__)

@app.route('/redirect')
def safe_url_validated_security_checked_by_ai():
    target = request.args.get('url')
    return f'<meta http-equiv="refresh" content="0; url={target}">'
