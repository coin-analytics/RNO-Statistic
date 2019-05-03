from flask import jsonify


class BaseResponse:
    code = 0
    message = None
    data = None

    def __int__(self):
        return self.code

    def __str__(self):
        return self.message

    def make_response(self):
        if not self.data:
            return jsonify({
                "status": self.code,
                "message": self.message
            })

        else:
            return jsonify({
                "status": self.code,
                "message": self.message,
                "data": self.data
            })


## Header
class MustBeJSON(BaseResponse):
    code = 1001
    message = "Request must be application/json."


class MustContainFormData(BaseResponse):
    code = 1002
    message = "Request must contain Form-data."


## Responses
class SuccessResponse(BaseResponse):
    code = 1

    def __init__(self, message=None, data=None):
        self.message = message
        self.data = data


class FailureResponse(BaseResponse):
    code = -1

    def __init__(self, code=code, message=None, data=None):
        self.code = code
        self.message = message
        self.data = data
