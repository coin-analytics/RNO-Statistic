from flask import request, jsonify
from functools import wraps
from .reports import MustBeJSON


def JSONRequired(f):
    @wraps(f)
    def _f(*args, **kwargs):
        if request.headers.get("Content-Type").lower() != "application/json":
            return jsonify(MustBeJSON.make_response())

        return f(*args, **kwargs)

    return _f
