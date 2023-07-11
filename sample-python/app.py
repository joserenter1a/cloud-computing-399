import os
from flask import Flask

app = Flask(__name__)
@app.route('/')
def sample():
	target = os.environ.get('TARGET', 'Jose')
	return f'Hello {target}!\n'

if __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0', port=int(os.environ.get('PORT', 8080)))
