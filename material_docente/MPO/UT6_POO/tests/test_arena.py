import unittest

from arena import Arena
from combate import Combate
from guerrero import Guerrero
from mago import Mago
from personaje import Personaje


class TestPersonajes(unittest.TestCase):
    def test_guerrero_nuevo(self):
        guerrero = Guerrero("Ada")
        self.assertEqual(guerrero.vida, 120)
        self.assertEqual(guerrero.atacar(), 14)

    def test_mago_nuevo(self):
        mago = Mago("Leo")
        self.assertEqual(mago.vida, 80)
        self.assertEqual(mago.mana, 9)

    def test_secuencia_de_ataques_del_mago(self):
        mago = Mago("Leo")
        self.assertEqual([mago.atacar() for _ in range(4)], [18, 18, 18, 4])
        self.assertEqual(mago.mana, 0)

    def test_dano_excesivo_deja_vida_a_cero(self):
        personaje = Personaje("Nora")
        personaje.recibir_danio(500)
        self.assertEqual(personaje.vida, 0)
        self.assertFalse(personaje.esta_vivo())

    def test_derrotado_no_puede_atacar(self):
        personaje = Personaje("Nora")
        personaje.recibir_danio(100)
        with self.assertRaises(RuntimeError):
            personaje.atacar()

    def test_validaciones_de_nombre_y_dano(self):
        with self.assertRaises(ValueError):
            Personaje("   ")
        personaje = Personaje("Nora")
        with self.assertRaises(ValueError):
            personaje.recibir_danio(-1)


class TestCombate(unittest.TestCase):
    def test_combate_devuelve_vencedor_y_registro(self):
        guerrero = Guerrero("Ada")
        mago = Mago("Leo")
        combate = Combate(guerrero, mago)
        vencedor = combate.combatir()
        self.assertIs(vencedor, guerrero)
        self.assertIs(combate.perdedor, mago)
        self.assertTrue(any("Vence Ada" in linea for linea in combate.registro()))

    def test_no_se_puede_repetir_un_combate(self):
        combate = Combate(Guerrero("Ada"), Mago("Leo"))
        combate.combatir()
        with self.assertRaises(RuntimeError):
            combate.combatir()

    def test_no_se_puede_luchar_contra_si_mismo(self):
        personaje = Personaje("Nora")
        with self.assertRaises(ValueError):
            Combate(personaje, personaje)


class TestArena(unittest.TestCase):
    def test_rechaza_nombres_duplicados(self):
        arena = Arena()
        arena.agregar(Guerrero("Ada"))
        with self.assertRaises(ValueError):
            arena.agregar(Mago("ada"))

    def test_dos_arenas_no_comparten_colecciones(self):
        primera = Arena()
        segunda = Arena()
        primera.agregar(Guerrero("Ada"))
        self.assertEqual(len(primera.personajes()), 1)
        self.assertEqual(len(segunda.personajes()), 0)
        self.assertEqual(primera.historial(), [])
        self.assertEqual(segunda.historial(), [])

    def test_historial_se_guarda_al_terminar(self):
        arena = Arena()
        arena.agregar(Guerrero("Ada"))
        arena.agregar(Mago("Leo"))
        vencedor = arena.enfrentar("Ada", "Leo")
        historial = arena.historial()
        self.assertEqual(len(historial), 1)
        self.assertEqual(historial[0]["vencedor"], vencedor.nombre)
        self.assertEqual(historial[0]["perdedor"], "Leo")

    def test_arena_rechaza_personaje_derrotado(self):
        arena = Arena()
        guerrero = Guerrero("Ada")
        mago = Mago("Leo")
        arena.agregar(guerrero)
        arena.agregar(mago)
        arena.enfrentar("Ada", "Leo")
        with self.assertRaises(ValueError):
            arena.enfrentar("Ada", "Leo")


if __name__ == "__main__":
    unittest.main()
