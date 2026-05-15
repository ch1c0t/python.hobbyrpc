from hobbyrpc import Client

def test_werkzeug(werkzeug_app):
    call = Client(
        address=werkzeug_app.address,
    )

    string = call('SomeName')

    assert string == {
        "status": "success",
        "received": {
            "fn": "SomeName",
        },
        "message": "Data processed successfully",
    }
