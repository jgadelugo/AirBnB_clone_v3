#!/usr/bin/python3
# return app_views status as JSON
from api.v1.views import app_views
"""Return status of API."""


@app_views.route('/status')
def appviews():
    """Get status of API."""
    return {
        "status": "OK",
    }
