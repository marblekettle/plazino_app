from flask import Flask, render_template
from os import path
from werkzeug import exceptions as ex
import json

def hello():
    return render_template('hello.html')

def handle_not_found(e):
    return render_template('notfound.html'), 404

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is not None:
        app.config.from_mapping(test_config)
    elif path.isfile(path.join(app.instance_path, 'config.json')):
        app.config.from_file('config.json', load=json.load)
    else:
        app.config.from_mapping({
            'TESTING': True,
            'SECRET_KEY':'dev',
        })
    app.add_url_rule('/', view_func=hello)
    app.register_error_handler(404, handle_not_found)
    return app
