#!/usr/bin/python3
"""Return status of API."""
from api.v1.views import app_views
from models.storage import count
@app_views.route('/status')
def appviews():
    """Get status of API."""
    return {"status": "OK"}


@app_view.route('/stats')
def stats():
    """retrieves the number of each objects by type."""
    return {"amenities": count("Amenities"), 
       	      "cities": count("Cities"),
              "places": count("Places"),
              "reviews": count("Reviews"),
              "states": count("States"),
              "users": count("Users")}
