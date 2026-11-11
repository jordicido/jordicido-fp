from combate import Combate


class Arena:
    """Colección de personajes y resultados de sus combates."""

    def __init__(self):
        self._personajes = []
        self._historial = []

    def agregar(self, personaje):
        if any(
            existente.nombre.casefold() == personaje.nombre.casefold()
            for existente in self._personajes
        ):
            raise ValueError("Ya existe un personaje con ese nombre")
        self._personajes.append(personaje)

    def personajes(self):
        return list(self._personajes)

    def buscar(self, nombre):
        for personaje in self._personajes:
            if personaje.nombre.casefold() == nombre.casefold():
                return personaje
        raise ValueError(f"No existe el personaje: {nombre}")

    def enfrentar(self, nombre_a, nombre_b):
        personaje_a = self.buscar(nombre_a)
        personaje_b = self.buscar(nombre_b)
        combate = Combate(personaje_a, personaje_b)
        vencedor = combate.combatir()
        self._historial.append(
            {
                "vencedor": vencedor.nombre,
                "perdedor": combate.perdedor.nombre,
                "registro": combate.registro(),
            }
        )
        return vencedor

    def historial(self):
        return [
            {
                "vencedor": entrada["vencedor"],
                "perdedor": entrada["perdedor"],
                "registro": list(entrada["registro"]),
            }
            for entrada in self._historial
        ]
