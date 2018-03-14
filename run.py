from eventlet import monkey_patch
monkey_patch()

from app import create_app, socketio

app = create_app()

from threading import Lock

thread = None
thread_lock = Lock()


def notifications_job():
    count = 0
    with app.app_context():
        step = int(app.config.get('STEP', 1))
        while True:
            socketio.sleep(10)
            count += step
            print("Count: {}".format(count))
            socketio.emit('my_response', {'count': count}, namespace='/rt/notifications/')


@socketio.on('connect', namespace='/rt/notifications/')
def start_notifications_thread():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=notifications_job)

if __name__ == '__main__':
    socketio.run(app, debug=True)