# Diseño y realización de pruebas

## Prueba de software

La prueba de software o testing es una práctica muy importante en el desarrollo de software, ya que nos ayuda a asegurar que nuestro programa funcione correctamente y esté libre de errores.

El testing es una parte fundamental del proceso de desarrollo, ya que garantiza la calidad del programa y permite detectar y solucionar errores antes de que llegue a los usuarios finales.

Existen diferentes tipos de pruebas, cada una con un objetivo específico, pero en general consisten en ejecutar casos de prueba o escenarios concretos con el objetivo de comprobar que el programa se comporta como se espera.

Es imposible probar todos los casos posibles, pero cuantas más pruebas se realicen y más completas sean, más se podrá reducir el riesgo de errores.

## Etapas del proceso de prueba

Hay distintas etapas en el proceso de testing:

1. **Planificación de la prueba**: En esta fase se definen los objetivos de las pruebas, se crea un plan de prueba y se seleccionan las herramientas y recursos necesarios.
2. **Creación de los casos de prueba**: Se diseñan los casos de prueba, que son escenarios concretos que se desean verificar. Esto incluye los pasos a seguir, los datos de entrada y los resultados esperados.
3. **Ejecución de los casos de prueba**: Se llevan a cabo los casos de prueba siguiendo los pasos definidos y comprobando que el programa devuelve los resultados esperados.
4. **Análisis de resultados**: Se revisan los resultados obtenidos, se registran los errores encontrados y se decide qué acciones tomar para solucionarlos
5. **Regresión**: Una vez corregidos los errores, se repiten las pruebas (paso 3) para asegurar que los cambios no han afectado negativamente a otras partes del programa.
6. **Aceptación**: Cuando todos los casos de prueba se han superado y se ha realizado una regresión adecuada, se considera que el programa está listo para ser entregado al cliente o puesto en producción.

## Clasificación de las pruebas

### Según su realización

- Pruebas manuales: Son realizadas por una persona que ejecuta los casos de prueba y analiza los resultados. Este tipo se utiliza especialmente cuando se requiere una evaluación visual o comprobar el comportamiento del programa en situaciones diversas.
- Pruebas automatizadas: Son realizadas mediante herramientas o programas específicos. Se utilizan para monitorizar cambios en el software y detectar incidencias. Son útiles para reducir el tiempo de prueba y asegurar que todos los casos se ejecutan de forma consistente.

### Según el conocimiento del sistema

- **Pruebas de caja negra**: Validan el comportamiento del programa sin tener en cuenta su implementación interna. Se basan en las especificaciones, entradas y salidas, sin necesidad de acceso al código fuente.
- **Pruebas de caja blanca**: Validan el comportamiento considerando la implementación interna del programa. Requieren acceso al código y el uso de técnicas como el análisis o revisión del código para verificar que se cumplen los criterios de calidad.

### Según su propósito

- **Pruebas unitarias**: Verifican el correcto funcionamiento de cada unidad o módulo individual del programa. Su objetivo es asegurarse de que cada parte funciona correctamente de forma aislada.
- **Pruebas de integración**: Verifican que las distintas unidades o módulos funcionan correctamente al interactuar entre ellos, para detectar errores en la integración.
- **Pruebas de sistema**: Evalúan el funcionamiento del programa como un todo, asegurando que cumple con los requisitos globales y está listo para su entrega o producción.
- **Pruebas de validación**: Verifican que el programa cumple con los requisitos del cliente o usuario final. Se asegura que el software hace lo que se espera.
- **Pruebas de carga**: Evalúan cómo se comporta el programa bajo una carga de trabajo elevada. El objetivo es garantizar que el sistema puede manejar la carga prevista sin fallos.
