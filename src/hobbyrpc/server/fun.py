from json import dumps
from pydantic import create_model

def call(self, input=None):
    if input:
        self.input = input

        Model = getattr(self.__class__, 'PydanticModel', None)
        if Model:
            self.pydantic = Model(**input)

    return self.call()

def json(self, input=None):
    output = self(input)

    Model = getattr(self.__class__, 'PydanticModel', None)
    if Model and isinstance(output, Model):
        return output.model_dump_json()
    else:
        return dumps(output)

def change(cl):
    # Map annotations to the (type, default) format required by create_model
    fields = {
        name: (type_hint, getattr(cl, name, ...))
        for name, type_hint in cl.__annotations__.items()
    }

    if fields:
        cl.PydanticModel = create_model('PydanticModel', **fields)

    cl.__call__ = call
    cl.json = json
