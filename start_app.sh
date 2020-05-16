#!/bin/sh

export FLASK_APP=rpi_flask_app.py
#flask run --host=0.0.0.0 -d
gunicorn --bind 0.0.0.0:5000 wsgi:app
