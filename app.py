import json
import os

from flask import Flask, make_response, render_template, request
from flask_cors import cross_origin

app = Flask(__name__,
			static_url_path='',
			static_folder='static',
			template_folder='templates')

app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
app.config.update(
	SESSION_COOKIE_SECURE=True,
	SESSION_COOKIE_HTTPONLY=True,
	SESSION_COOKIE_SAMESITE='Lax',
)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1800


@app.route("/", methods=['GET'])
def index():
	response = make_response(render_template('index.html',))
	# response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
	# response.headers['X-Content-Type-Options'] = 'nosniff'
	# response.headers['X-Frame-Options'] = 'SAMEORIGIN'
	# response.headers['X-XSS-Protection'] = '1; mode=black'
	return response

if __name__ == '__main__':
	app.run(port = os.environ.get("PORT", 8080))
