import json
from werkzeug.wrappers import Request, Response

import sys
import logging

logging.basicConfig(
    stream=sys.stderr,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BadRequest(Exception):
    pass

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
        logging.exception(f"An Exception happened while processing the request: {e}")
        return Response("400", status=400)
