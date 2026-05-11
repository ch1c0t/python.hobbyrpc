from http.client import HTTPConnection

def test_its_response(tcp_server):
    c = HTTPConnection('127.0.0.1', 8080)

    c.request('OPTIONS', '/')
    response = c.getresponse()

    assert response.status == 200

    header = response.getheader('Access-Control-Allow-Headers')
    assert header == 'Authorization, Content-Type'

# from pprint import pprint as p
# def test_its_info(tcp_server):
#     p(dir(tcp_server))
#     p(vars(tcp_server))
