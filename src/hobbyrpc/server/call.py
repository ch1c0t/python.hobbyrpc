import json
from werkzeug.wrappers import Request, Response

from .logger import logger
from .exceptions import BadRequest

@Request.application
def call(self, request):
    try:
        match request.method:
            case 'POST':
                data = request.get_json()
                fn = data['fn']

                if fn in self.functions:
                    result = self.functions[fn]()

                    return Response(
                        json.dumps(result),
                        mimetype='application/json',
                        status=200,
                    )
                else:
                    raise BadRequest
            case _:
                raise BadRequest
    except Exception as e:
        logger.exception(f"An Exception happened while processing the request: {e}")
        return Response("400", status=400)
