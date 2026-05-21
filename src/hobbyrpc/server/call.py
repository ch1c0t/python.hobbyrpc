from copy import copy
from werkzeug.wrappers import Request, Response
from .exceptions import Error, BadRequest

@Request.application
def call(self, request):
    try:
        user = self.current_user(request)

        match request.method:
            case 'POST':
                data = request.get_json()
                fn = data['fn']

                if fn in self.functions:
                    fun = self.functions[fn]
                    if user:
                        fun = copy(fun)
                        fun.user = user

                    input = data.get('in')
                    json = fun.json(input)

                    return Response(
                        json,
                        mimetype='application/json',
                        status=200,
                    )
                else:
                    raise BadRequest
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
