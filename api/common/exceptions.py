from werkzeug.exceptions import (
    Conflict,
    NotFound,
    Unauthorized,
    BadRequest,
)


class JSONException(Exception):
    status_code = NotFound.code
    message = ""

    def __init__(self, message=None, status_code=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            "error": {
                "code": self.status_code,
                "message": self.message,
                "type": str(self.__class__.__name__),
            }
        }


class InvalidContentType(JSONException):
    pass


class InvalidPermissions(JSONException):
    status_code = Unauthorized.code


class InvalidAPIRequest(JSONException):
    pass


class DatabaseError(JSONException):
    pass


class RecordNotFound(DatabaseError):

    pass


class RecordAlreadyExists(DatabaseError):
    status_code = Conflict.code


class MissingArguments(Exception):
    status_code = BadRequest.code


class TypeErrorFlusk(InvalidAPIRequest):
    status_code = BadRequest.code


class InvalidURL(InvalidAPIRequest):
    pass


class YouAreNotAdmin(InvalidPermissions):
    pass


class CannotChangeOthersData(InvalidPermissions):
    pass


class CannotDeleteOthersData(InvalidPermissions):
    pass


class CannotHaveMultipleRoles(DatabaseError):
    message = "There are multiple roles in a user, contact the database administrator"
