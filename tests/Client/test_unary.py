from hobbyrpc import Client
from tests.helpers.d import d

def test_Compile_with_safety_wrapper(coffeerpc_server):
    call = Client(coffeerpc_server.address)

    output = call('Compile', code='answer = 42')
    string = """
      (function() {
        var answer;

        answer = 42;

      }).call(this);
    """
    assert output == d(string)

def test_Compile_without_safety_wrapper(coffeerpc_server):
    call = Client(coffeerpc_server.address)

    output = call('Compile', code='answer = 42', bare=True)
    string = """
        var answer;

        answer = 42;
    """
    assert output == d(string)
