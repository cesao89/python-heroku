import os
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'Hello {}! - Version {}'.format(name if name else 'World!', os.environ.get('BUILDNO', None))


@app.route('/docs/<path:path>')
def doc(path):
    return send_from_directory('static/docs', path)

SWAGGER_URL = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    '/docs/swagger.json',
    config={ 'app_name': 'NeoTalk Web' }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)