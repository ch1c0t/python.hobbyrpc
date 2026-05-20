from json import dumps

def json(self, input=None):
    output = self(input)

    Model = getattr(self.__class__, 'PydanticModel', None)
    if Model and isinstance(output, Model):
        return output.model_dump_json()
    else:
        return dumps(output)
