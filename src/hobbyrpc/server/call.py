from werkzeug.wrappers import Request, Response
from .exceptions import Error, BadRequest

@Request.application
def call(self, request):
    try:
        user = self.current_user(request)
        origin = self.origin_of(request)

        match request.method:
            case 'POST':
                response = self.response_to_POST(
                    request=request,
                    user=user,
                )
            case 'OPTIONS':
                response = self.response_to_OPTIONS(request)
            case _:
                raise BadRequest

        response.headers['Access-Control-Allow-Origin'] = origin

        return response
    except Exception as e:
        self.logger.exception(f"An Exception happened while processing the request: {e}")
        match e:
            case Error():
                status = e.status
                string = str(status)
                return Response(string, status=status)
            case _:
                return Response("400", status=400)
