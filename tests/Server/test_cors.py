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

        response = post(
            address,
            json={'fn': 'ListNames'},
        )
        assert response.status_code == 200
        assert response.json() == ['default']
        assert response.headers['Access-Control-Allow-Origin'] == '*'

def test_custom_CORS_headers(cors_rpc):
    address = cors_rpc.address
    if not address.startswith('/'):
        response = options(address)
        assert response.status_code == 200

        headers = response.headers
        assert headers['Access-Control-Allow-Methods'] == 'GET, POST, OPTIONS'
        assert headers['Access-Control-Allow-Headers'] == 'Authorization, Content-Type, Content-Length'
        assert headers['Access-Control-Max-Age'] == '80000'

        response = post(
            address,
            json={'fn': 'SomeFunction'},
        )
        assert response.status_code == 200
        assert response.json() == ['custom', 'headers']

def test_restricting_CORS_origins(cors_with_restricted_origins_rpc):
    address = cors_with_restricted_origins_rpc.address
    if not address.startswith('/'):
        response = post(
            address,
            json={'fn': 'SomeFunction'},
            headers={
                'Content-Type': 'application/json',
                'Origin': 'https://not.allowed.domain',
            }
        )
        assert response.status_code == 400

        response = post(
            address,
            json={'fn': 'SomeFunction'},
            headers={
                'Content-Type': 'application/json',
                'Origin': 'https://web.allowed.domain',
            }
        )
        assert response.status_code == 200
        assert response.json() == ['custom', 'origins']
