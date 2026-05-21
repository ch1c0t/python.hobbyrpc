from json import dumps
from pydantic import BaseModel

def json(self, input=None):
    output = self(input)

    if isinstance(output, BaseModel):
        return output.model_dump_json()
    else:
        return dumps(output)
