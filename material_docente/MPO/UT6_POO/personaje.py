class Personaje:
    """Personaje base con vida y ataque común."""

    VIDA_MAXIMA = 100

    def __init__(self, nombre, vida=VIDA_MAXIMA):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if isinstance(vida, bool) or not isinstance(vida, (int, float)):
            raise TypeError("La vida debe ser numérica")
        if vida <= 0:
            raise ValueError("La vida inicial debe ser positiva")
        self.nombre = nombre.strip()
        self.vida_maxima = vida
        self.vida = vida

    def atacar(self):
        self._comprobar_vivo()
        return 6

    def recibir_danio(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise TypeError("El daño debe ser numérico")
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo")
        self.vida = max(0, self.vida - cantidad)

    def esta_vivo(self):
        return self.vida > 0

    def _comprobar_vivo(self):
        if not self.esta_vivo():
            raise RuntimeError("Un personaje derrotado no puede atacar")

    def __str__(self):
        return f"{self.nombre} ({self.vida}/{self.vida_maxima} PV)"
