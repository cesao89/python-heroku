import os
from io import BytesIO
from flask import Flask, request, send_from_directory, send_file, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from c0d1h3r0ku.handlers.neotalkMock import Chatbot, User

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'Hello {}! - Version {}'.format(name if name else 'World!', os.environ.get('BUILDNO', None))


@app.route('/neotalk/chatbot/send-message', methods=["POST"])
def send_message():
    h = Chatbot()
    return h.send_message(request)


@app.route('/neotalk/user/recovery-password', methods=['POST'])
def recovery_password():
    h = User()
    return h.recovery_password(request)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        directory='c0d1h3r0ku/static',
        filename='dummy.pdf',
        mimetype='application/pdf',
        as_attachment=True
    )


@app.route('/docs/<path:path>')
def doc(path):
    return send_from_directory('c0d1h3r0ku/static/docs', path)


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