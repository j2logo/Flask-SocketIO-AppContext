from flask import Blueprint

real_time_events = Blueprint('real_time_events', __name__)

from . import events
