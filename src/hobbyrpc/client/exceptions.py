class Error(Exception):
    pass

class BadRequest(Error):
    pass

class Forbidden(Error):
    pass

class UnexpectedStatus(Error):
    pass

class NotImplementedScheme(Error):
    pass
