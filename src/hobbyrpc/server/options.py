from werkzeug.wrappers import Response

class OPTIONS:
    def response_to_OPTIONS(self, request):
        response = Response(status=200)

        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
        response.headers['Access-Control-Max-Age'] = '86400'

        return response
