from flask import request, jsonify
from functools import wraps
from .reports import MustBeJSON, MustContainFormData


def JSONRequired(f):
    @wraps(f)
    def _f(*args, **kwargs):
        if request.headers.get("Content-Type").lower() != "application/json":
            return jsonify(MustBeJSON().make_response())

        return f(*args, **kwargs)

    return _f


def FormDataRequired(*keys):
    def decorator(f):
        @wraps(f)
        def _f(*args, **kwargs):
            if not request.form:            return MustContainFormData().make_response()

            ProvidenKeys =                  {*keys}
            if not ProvidenKeys:            return f(*args, **kwargs)

            FormKeys =                      {*request.form}
            if FormKeys != ProvidenKeys:    return MustContainFormData().make_response()

            return f(*args, **kwargs)
        return _f

    return decorator
