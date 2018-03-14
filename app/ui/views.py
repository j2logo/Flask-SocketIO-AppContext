from flask import render_template

from . import ui


@ui.route('/')
def index():
    return render_template('ui/index.html')
