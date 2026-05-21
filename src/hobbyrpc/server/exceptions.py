class Error(Exception):
    def status(self):
        return self.__class__.status

class BadRequest(Error):
    status = 400

class Forbidden(Error):
    status = 403
