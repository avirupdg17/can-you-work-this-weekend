from gevent.pywsgi import WSGIServer
import os
import sys
from inspect import getsourcefile
from flask_app.routes import app

path_folders = os.environ['PATH'].split(':')
current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))

if current_dir not in path_folders:
    sys.path.append(current_dir)

ip = '0.0.0.0'
port = 5001

http_server = WSGIServer((ip, port), app)

print("Serving on address", ip, "port", port)
http_server.serve_forever()