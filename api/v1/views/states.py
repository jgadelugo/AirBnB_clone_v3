#!/usr/bin/python3
"""States view."""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Retrieves the list of all State objects."""
    if request.method == 'GET':
        states = []
        for v in storage.all('State').values():
            states.append(v.to_dict())
        return (jsonify(states), 200)
    elif request.method == 'POST': 
        """Create a new State object with request."""
        if not request.is_json:
            return ("Not a JSON", 400)
        body = request.get_json()
        if 'name' not in body.keys():
            return ("Missing name", 400)
        return State(body).to_dict(), 200

@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def get_state(state_id):
    """Retrieve a state by id."""
    if request.method == 'GET':
        for v in storage.all('State').values():
            if v.id == state_id:
                return (v.to_dict(), 200)
        abort(404)
#    elif request.method == 'PUT':
        
