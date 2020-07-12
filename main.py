import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'Hello {}! - Version {}'.format(name if name else 'World!', os.environ.get('BUILDNO', None))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)