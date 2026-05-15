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
def application(request):
    try:
        match request.method:
            case 'POST':
                data = request.get_json()

                if data['fn'] is not None:
                    result = {
                        "status": "success",
                        "received": data,
                        "message": "Data processed successfully"
                    }

                    # mimetype sets the correct 'Content-Type: application/json' header
                    return Response(
                        json.dumps(result),
                        mimetype='application/json',
                        status=200
                    )
                else:
                    raise BadRequest
            case _:
                return Response("400", status=400)
    except Exception as e:
        logging.exception("An Exception happened while processing the request:")
        return Response("400", status=400)
