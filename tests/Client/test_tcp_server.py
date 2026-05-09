from http.client import HTTPConnection

def test_tcp_server(tcp_server):
    c = HTTPConnection('127.0.0.1', 8080)

    c.request('OPTIONS', '/')
    response = c.getresponse()

    assert response.status == 200

    header = response.getheader('Access-Control-Allow-Headers')
    assert header == 'Authorization, Content-Type'
