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
        #Create a new State object with request.
        if not request.is_json:
            return ("Not a JSON", 400)
        body = request.get_json()
        if 'name' not in body.keys():
            return ("Missing name", 400)
        body.save()
        return State(body).to_dict(), 200

@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def state(state_id):
    """Retrieve a state by id."""
    found = False
    for v in storage.all('State').values():
        if v.id == state_id:
            found = True
            break
    if request.method == 'GET':
        if found:
            return (v.to_dict(), 200)
        else:
            abort(404)
    elif request.method == 'PUT':
        #Update a State object
        if not found:
            abort(404)
        if not request.is_json:
            return ("Not a JSON", 400)
        body = request.get_json()
        for key, value in body:
            if key != 'id'  or key != 'created_at' or key != 'updated_at':
                setattr(v, key, value)
        v.save()
        return (v, 200)

