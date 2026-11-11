class Combate:
    """Combate determinista entre dos personajes."""

    def __init__(self, personaje_a, personaje_b):
        if personaje_a is personaje_b:
            raise ValueError("Un personaje no puede enfrentarse a sí mismo")
        if not personaje_a.esta_vivo() or not personaje_b.esta_vivo():
            raise ValueError("Los dos personajes deben estar vivos")
        self.personaje_a = personaje_a
        self.personaje_b = personaje_b
        self._registro = []
        self._ejecutado = False
        self.vencedor = None
        self.perdedor = None

    def combatir(self):
        if self._ejecutado:
            raise RuntimeError("El combate ya ha terminado")

        atacante = self.personaje_a
        defensor = self.personaje_b
        self._registro.append(
            f"Comienza el combate: {self.personaje_a.nombre} contra "
            f"{self.personaje_b.nombre}."
        )

        while self.personaje_a.esta_vivo() and self.personaje_b.esta_vivo():
            dano = atacante.atacar()
            defensor.recibir_danio(dano)
            self._registro.append(
                f"{atacante.nombre} ataca a {defensor.nombre} con {dano} "
                f"de daño ({defensor.vida} PV restantes)."
            )
            if not defensor.esta_vivo():
                self.vencedor = atacante
                self.perdedor = defensor
                self._registro.append(f"Vence {self.vencedor.nombre}.")
                break
            atacante, defensor = defensor, atacante

        self._ejecutado = True
        return self.vencedor

    def registro(self):
        return list(self._registro)
