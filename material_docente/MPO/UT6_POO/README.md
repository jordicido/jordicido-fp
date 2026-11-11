# Solución de referencia docente — Arena de héroes

Esta carpeta contiene una solución funcional de referencia para el profesorado.
No forma parte del sitio público: está fuera de `docs/` y no se enlaza desde la
navegación de MkDocs.

## Ejecución

Desde esta carpeta:

```bash
python main.py
python -m unittest discover -s tests -v
```

La solución utiliza únicamente la biblioteca estándar. El menú se encuentra en
`main.py`; las reglas del dominio están en módulos separados para que puedan
probarse sin `input()`.

## Decisiones de diseño

- El primer personaje recibe el primer turno y los turnos se alternan.
- Un combate solo acepta personajes distintos y vivos al comenzar.
- Al terminar, el combate queda marcado como ejecutado y no se puede repetir.
- La arena guarda referencias a instancias, no diccionarios, y crea sus propias
  listas para evitar estado compartido accidental.
- Se permite que un personaje herido permanezca en la arena, pero no puede
  iniciar otro combate si está derrotado. El historial conserva vencedor,
  perdedor y registro legible.
- `atacar()` calcula el daño; `Combate` lo aplica con `recibir_danio()`.
