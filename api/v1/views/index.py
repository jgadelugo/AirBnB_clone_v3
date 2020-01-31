#!/usr/bin/python3
"""Return status of API."""
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def appviews():
    """Get status of API."""
    return {"status": "OK"}


@app_views.route('/stats')
def stats():
    """retrieves the number of each objects by type."""
    return {
        "amenities": storage.count("Amenities"),
        "cities": storage.count("Cities"),
        "places": storage.count("Places"),
        "reviews": storage.count("Reviews"),
        "states": storage.count("States"),
        "users": storage.count("Users")}
