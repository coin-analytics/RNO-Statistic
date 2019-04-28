class BaseErrorCode:
    code = 0
    message = ""

    def __int__(self):
        return self.code

    def __str__(self):
        return self.message

    @classmethod
    def make_response(cls):
        return {
            "status": cls.code,
            "message": cls.message
        }


## Header
class MustBeJSON(BaseErrorCode):
    code = 1
    message = "Request must be application/json."
