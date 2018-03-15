from threading import Lock

from flask import current_app

from .. import socketio

thread = None
thread_lock = Lock()


def notifications_job(app):
    count = 0
    with app.app_context():
        step = int(app.config.get('STEP', 1))
        while True:
            socketio.sleep(10)
            count += 1
            socketio.emit('my_response', {'count': count}, namespace='/rt/notifications/')


@socketio.on('connect', namespace='/rt/notifications/')
def start_notifications_thread():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(notifications_job, current_app._get_current_object())
