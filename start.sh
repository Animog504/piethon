#!/usr/bin/env bash
pip install flask
pip install flask-socketio
pip install parse
pip install gevent
FLASK_APP=server.py FLASK_DEBUG=1 flask run