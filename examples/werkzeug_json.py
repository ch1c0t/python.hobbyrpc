import json
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    if request.method == 'POST':
        # 1. Parse incoming JSON data if needed
        # Use silent=True to avoid crashing on empty/invalid bodies
        data = request.get_json(silent=True) 
        
        # 2. Prepare your response data
        result = {
            "status": "success",
            "received": data,
            "message": "Data processed successfully"
        }

        # 3. Create the JSON response
        # mimetype sets the correct 'Content-Type: application/json' header
        return Response(
            json.dumps(result), 
            mimetype='application/json',
            status=200
        )

    # Basic fallback for other methods
    return Response("Please use POST.", status=405)
