def call(self, input=None):
    if input:
        self.input = input

        Model = getattr(self.__class__, 'PydanticModel', None)
        if Model:
            self.pydantic = Model(**input)

            for field, value in self.pydantic.model_dump().items():
                setattr(self, field, value)

    return self.call()
