from ..blueprint import RSBlueprint
from flask import make_response, jsonify


RS_API = RSBlueprint("RNOStatistics API", __name__, prefix="/api/")

