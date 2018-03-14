from flask import Flask
from flask_socketio import SocketIO

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'eventlet'
socketio = SocketIO(async_mode=async_mode)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Blueprints registration
    from app.api import api_bp
    app.register_blueprint(api_bp)

    from app.ui import ui
    app.register_blueprint(ui)

    from app.rt import events
    socketio.init_app(app)

    return app
