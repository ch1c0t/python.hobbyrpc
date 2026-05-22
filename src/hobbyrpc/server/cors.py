from .exceptions import BadOrigin, BadSetting

class CORS:
    def origin_of(self, request):
        origins = self.CORS['origins']

        match origins:
            case '*':
                return '*'
            case list():
                origin = request.headers['Origin']

                if origin in origins:
                    return origin
                else:
                    raise BadOrigin
            case _:
                raise BadSetting
