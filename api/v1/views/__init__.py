#!/usr/bin/python3
# create app_views blueprint
from flask import Blueprint
app_views = Blueprint('/api/v1/app_views', __name__)
from api.v1.views.index import *
