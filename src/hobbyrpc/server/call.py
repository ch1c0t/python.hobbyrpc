from werkzeug.wrappers import Request, Response

from .exceptions import BadRequest

@Request.application
def call(self, request):
    try:
        match request.method:
            case 'POST':
                data = request.get_json()
                fn = data['fn']

                if fn in self.functions:
                    fun = self.functions[fn]
                    if 'in' in data:
                        json = fun.json(data['in'])
                    else:
                        json = fun.json()

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
        return Response("400", status=400)
