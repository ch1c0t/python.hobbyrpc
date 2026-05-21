from copy import copy
from werkzeug.wrappers import Request, Response
from .exceptions import BadRequest, Forbidden

@Request.application
def call(self, request):
    try:
        if self.is_auth_required():
            token = request.headers.get('Authorization')
            if not token:
                raise Forbidden

            user = self.find_user(token)
            if not user:
                raise Forbidden
        else:
            user = None

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
            case BadRequest():
                return Response("400", status=400)
            case Forbidden():
                return Response("403", status=403)
            case _:
                return Response("400", status=400)
