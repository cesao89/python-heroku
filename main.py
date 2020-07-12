import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'Hello {}!'.format(name if name else 'World!')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)