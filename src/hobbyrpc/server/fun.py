def call(self, input=None):
    if input:
        self.input = input

    return self.call()

def change(cl):
    cl.__call__ = call
