from werkzeug.wrappers import Request, Response
from .exceptions import Error, BadRequest

@Request.application
def call(self, request):
    try:
        user = self.current_user(request)

        match request.method:
            case 'POST':
                return self.response_to_POST(
                    request=request,
                    user=user,
                )
            case 'OPTIONS':
                return self.response_to_OPTIONS(request)
            case _:
                raise BadRequest
    except Exception as e:
        self.logger.exception(f"An Exception happened while processing the request: {e}")
        match e:
            case Error():
                status = e.status
                string = str(status)
                return Response(string, status=status)
            case _:
                return Response("400", status=400)
