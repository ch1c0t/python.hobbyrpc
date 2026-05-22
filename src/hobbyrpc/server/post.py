from copy import copy
from werkzeug.wrappers import Response
from .exceptions import BadRequest

class POST:
    def response_to_POST(self, request, user=None):
        mimetype = request.headers.get('Content-Type', '')
        if not mimetype.startswith('application/json'):
            raise BadRequest

        data = request.get_json()
        fn = data['fn']

        if fn in self.functions:
            fun = self.functions[fn]
            if user:
                fun = copy(fun)
                fun.user = user

            input = data.get('in')
            json = fun.json(input)

            response = Response(
                json,
                mimetype='application/json',
                status=200,
            )

            return response
        else:
            raise BadRequest
