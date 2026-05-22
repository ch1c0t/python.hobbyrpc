from werkzeug.wrappers import Response

class OPTIONS:
    def response_to_OPTIONS(self, request):
        response = Response(status=200)

        response.headers['Access-Control-Allow-Methods'] = self.CORS['methods']
        response.headers['Access-Control-Allow-Headers'] = self.CORS['headers']
        response.headers['Access-Control-Max-Age'] = self.CORS['max_age']

        return response
