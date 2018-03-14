from threading import Lock
from flask import Flask
from app import create_app, socketio

thread = None
thread_lock = Lock()


def custom_create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # NO socketio initialization

    # Blueprints registration (only real time events blueprint)
    from app.rt import real_time_events
    app.register_blueprint(real_time_events)

    return app


def notifications_job():
    app = create_app()
    count = 0
    with app.app_context():
        while True:
            step = int(app.config.get('STEP', 1))
            count += step
            print("Count: {}".format(count))
            socketio.emit('my_response', {'count': count}, namespace='/rt/notifications/')
            socketio.sleep(10)


@socketio.on('connect', namespace='/rt/notifications/')
def start_notifications_thread():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=notifications_job)
