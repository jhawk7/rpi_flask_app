#!/bin/sh

export FLASK_APP=rpi_flask_app.py
gunicorn --bind 0.0.0.0:5000 wsgi:app
