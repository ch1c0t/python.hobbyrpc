from requests import post, options

def test_default_CORS_headers(bare_rpc):
    address = bare_rpc.address
    if not address.startswith('/'):
        response = options(address)
        assert response.status_code == 200

        headers = response.headers
        assert headers['Access-Control-Allow-Methods'] == 'POST, OPTIONS'
        assert headers['Access-Control-Allow-Headers'] == 'Authorization, Content-Type'
        assert headers['Access-Control-Max-Age'] == '86400'
