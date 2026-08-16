# Sistema de Restaurante — restaurante_app

**Estudiante:** [Nombre completo del estudiante]
**Semana:** 9
**Tema:** Estructuras de datos en Python (list, tuple, dict, set) aplicadas a `restaurante_app`

## Descripción del sistema

`restaurante_app` es un sistema de consola desarrollado en Python que administra
**productos** y **usuarios** de un restaurante. Esta entrega evoluciona el proyecto de
semanas anteriores incorporando de forma **funcional y justificada** las principales
estructuras de datos de Python (listas, tuplas, diccionarios y conjuntos) para
resolver necesidades reales del sistema: mantener colecciones dinámicas, representar
información estable, asociar relaciones clave → valor y obtener valores únicos sin
duplicados.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase Producto
│   └── usuario.py       # Clase Usuario
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase de servicio Restaurante
└── main.py               # Punto de arranque y menú interactivo
```

## Responsabilidad de cada componente

- **`Producto`** (`modelos/producto.py`): representa un producto del restaurante
  (código, nombre, categoría, precio, disponibilidad). El código se genera
  automáticamente desde el servicio `Restaurante`.
- **`Usuario`** (`modelos/usuario.py`): representa de forma general a una persona
  registrada en el sistema (identificación, nombre, correo). Todavía no define una
  jerarquía de tipos de usuario; esa especialización queda para una actividad futura.
- **`Restaurante`** (`servicios/restaurante.py`): servicio encargado de administrar
  las colecciones de productos y usuarios, y de todas las operaciones sobre ellas
  (registrar, buscar, actualizar, eliminar, listar). `main.py` nunca recorre ni
  modifica estas colecciones directamente; siempre lo hace a través de los métodos
  del servicio.
- **`main.py`**: contiene únicamente el menú interactivo, la solicitud de datos por
  consola, la creación de objetos y el manejo de errores de entrada, delegando toda
  la lógica de administración al servicio `Restaurante`.

## Uso de las estructuras de datos

- **`list` (lista):** en `Restaurante`, `self._productos` y `self._usuarios` son las
  colecciones dinámicas donde se registran, listan, actualizan y eliminan los
  objetos `Producto` y `Usuario` durante la ejecución del programa.
- **`tuple` (tupla):** en `main.py`, `OPCIONES_MENU` es una tupla con el texto de
  cada opción del menú principal. Al ser información que **no cambia** durante la
  ejecución, una tupla es la estructura adecuada para representarla, y se recorre
  para imprimir el menú cada vez que se muestra.
- **`dict` (diccionario):**
  - En `main.py`, la variable `opciones` asocia cada número de opción del menú
    (clave) con la función que debe ejecutarse (valor), evitando una larga cadena de
    `if/elif` y facilitando agregar nuevas opciones en el futuro.
  - En `Restaurante`, `self._indice_productos` asocia cada **código de producto**
    (clave) con su objeto `Producto` (valor), lo que permite buscar, actualizar y
    eliminar productos de forma directa y eficiente, sin recorrer toda la lista.
- **`set` (conjunto):** el método `Restaurante.obtener_categorias()` recorre todos
  los productos registrados y construye un conjunto con sus categorías, eliminando
  automáticamente los duplicados. `main.py` usa este conjunto para mostrar las
  categorías únicas en la opción "Mostrar categorías".

## Menú interactivo

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
```

Cada opción se ejecuta a través del diccionario de funciones definido en `main.py`,
y el programa se mantiene en ejecución hasta seleccionar la opción 9.

## Validaciones y manejo de errores

- Las entradas numéricas (precio) se validan en un bucle hasta recibir un valor
  correcto, sin detener el programa ante una entrada inválida.
- Las respuestas de sí/no se normalizan y validan de la misma forma.
- La actualización de productos permite dejar campos vacíos (Enter) para no
  modificarlos, sin sobrescribir información por error.
- El bucle principal del menú envuelve la ejecución de cada opción en un bloque
  `try/except`, de modo que un error inesperado se informe al usuario sin cerrar
  el programa.
- No se permiten códigos de producto ni identificaciones de usuario duplicados.

## Instrucciones de ejecución

1. Verificar que Python 3.9 o superior esté instalado.
2. Clonar el repositorio y ubicarse en la carpeta `restaurante_app`.
3. Ejecutar el programa:

```bash
python3 main.py
```

4. Utilizar el menú interactivo para registrar, buscar, actualizar, eliminar y
   listar productos; registrar y listar usuarios; y consultar las categorías
   únicas registradas.

## Reflexión

Elegir la estructura de datos adecuada según la necesidad del problema mejora tanto
el rendimiento como la claridad del código. Usar una lista para colecciones que
crecen y cambian, una tupla para datos que deben permanecer estables, un diccionario
cuando existe una relación directa de clave a valor, y un conjunto cuando se
necesita unicidad, evita soluciones improvisadas —como recorrer listas completas
para buscar un elemento o filtrar duplicados manualmente— y hace que la intención
del código sea mucho más explícita para cualquier persona que lo lea.
