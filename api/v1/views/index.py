#!/usr/bin/python3
# return app_views status as JSON
from api.v1.views import app_views


@app_views.route('/status')
"""Get status of API."""
def appviews():
    return {
        "status": "OK",
    }
