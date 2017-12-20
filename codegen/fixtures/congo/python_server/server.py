from app import app

import gevent
from gevent.pywsgi import WSGIServer
from gevent.pool import Pool
from gevent import monkey

import signal

# setting it to False will block gevent and setting it to True breaks js9. @TODO investigate why it breaks js9.
monkey.patch_all(subprocess=False)


server = WSGIServer(('', 5000), app, spawn=Pool(None))


def stop():
    server.stop()


gevent.signal(signal.SIGINT, stop)


if __name__ == "__main__":
    server.serve_forever()
