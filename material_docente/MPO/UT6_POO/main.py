from arena import Arena
from guerrero import Guerrero
from mago import Mago


def mostrar_menu():
    print("\n=== ARENA DE HÉROES ===")
    print("1. Crear guerrero")
    print("2. Crear mago")
    print("3. Mostrar personajes")
    print("4. Iniciar combate")
    print("5. Ver historial")
    print("0. Salir")


def ejecutar():
    arena = Arena()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        try:
            if opcion == "1":
                arena.agregar(Guerrero(input("Nombre: ")))
                print("Guerrero creado.")
            elif opcion == "2":
                arena.agregar(Mago(input("Nombre: ")))
                print("Mago creado.")
            elif opcion == "3":
                for personaje in arena.personajes():
                    print(personaje)
            elif opcion == "4":
                primero = input("Primer personaje: ")
                segundo = input("Segundo personaje: ")
                vencedor = arena.enfrentar(primero, segundo)
                print(f"Vence {vencedor.nombre}.")
            elif opcion == "5":
                for numero, entrada in enumerate(arena.historial(), start=1):
                    print(f"Combate {numero}: {entrada['vencedor']} vence a "
                          f"{entrada['perdedor']}")
            elif opcion == "0":
                print("Hasta pronto.")
                return
            else:
                print("Opción no válida.")
        except (ValueError, TypeError, RuntimeError) as error:
            print(f"No se puede realizar la operación: {error}")


if __name__ == "__main__":
    ejecutar()
