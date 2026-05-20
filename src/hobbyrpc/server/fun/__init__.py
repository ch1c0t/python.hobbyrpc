from pydantic import create_model

from .call import call
from .json import json

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
