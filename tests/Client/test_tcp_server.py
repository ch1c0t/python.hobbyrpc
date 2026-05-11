from http.client import HTTPConnection

def test_its_response(coffeerpc_server):
    c = HTTPConnection('127.0.0.1', 8080)

    c.request('OPTIONS', '/')
    response = c.getresponse()

    assert response.status == 200

    header = response.getheader('Access-Control-Allow-Headers')
    assert header == 'Authorization, Content-Type'

# from pprint import pprint as p
# def test_its_info(coffeerpc_server):
#     p(dir(coffeerpc_server))
#     p(vars(coffeerpc_server))
