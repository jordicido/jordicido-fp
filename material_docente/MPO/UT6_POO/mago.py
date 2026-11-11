from personaje import Personaje


class Mago(Personaje):
    """Mago de 80 PV: tres ataques mágicos y después ataques básicos."""

    MANA_INICIAL = 9
    COSTE_MAGIA = 3

    def __init__(self, nombre):
        super().__init__(nombre, vida=80)
        self.mana = self.MANA_INICIAL

    def atacar(self):
        self._comprobar_vivo()
        if self.mana >= self.COSTE_MAGIA:
            self.mana -= self.COSTE_MAGIA
            return 18
        return 4
