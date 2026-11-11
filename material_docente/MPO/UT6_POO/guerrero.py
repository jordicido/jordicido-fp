from personaje import Personaje


class Guerrero(Personaje):
    """Personaje resistente con un ataque de 14 puntos."""

    def __init__(self, nombre):
        super().__init__(nombre, vida=120)

    def atacar(self):
        self._comprobar_vivo()
        return 14
