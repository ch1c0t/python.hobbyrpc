from werkzeug.wrappers import Request, Response

from .logger import logger
from .to_json import to_json
from .exceptions import BadRequest

@Request.application
def call(self, request):
    try:
        match request.method:
            case 'POST':
                data = request.get_json()
                fn = data['fn']

                if fn in self.functions:
                    if 'in' in data:
                        result = self.functions[fn](data['in'])
                    else:
                        result = self.functions[fn]()

                    return Response(
                        to_json(result),
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
