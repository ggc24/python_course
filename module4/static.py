
def metodoestatico(f):
    def wrap(*args, **kwargs):
        print(*args)
        return f()
    return wrap


class Miclase:

    @metodoestatico
    def _metodo():
        print('Hola')

    def __init__(self, atributo):
        self.atributo = atributo

