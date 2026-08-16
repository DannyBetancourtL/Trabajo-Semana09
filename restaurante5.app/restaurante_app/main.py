"""Punto de arranque del Sistema de Restaurante.

Este modulo se encarga unicamente de la interaccion por consola:
mostrar el menu, solicitar datos al usuario, crear los objetos del
dominio y delegar toda la administracion de colecciones al servicio
Restaurante. No recorre ni modifica directamente las listas internas
del servicio.
"""

from typing import Callable, Dict, Tuple

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Tupla: representa la informacion estable de las opciones del menu.
# No cambia durante la ejecucion del programa, por lo que una tupla es
# la estructura adecuada para almacenarla.
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "----------------------------------------",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "----------------------------------------",
    "8. Mostrar categorías",
    "9. Salir",
)


def mostrar_encabezado(restaurante: Restaurante) -> None:
    """Imprime el encabezado con el nombre del restaurante."""
    print("=" * 35)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE ")
    print("=" * 35)
    print(f"Nombre: {restaurante.nombre}")


def cargar_datos_iniciales(restaurante: Restaurante) -> None:
    """Precarga productos y usuarios de ejemplo en el sistema."""
    restaurante.registrar_producto(
        Producto(restaurante.generar_codigo_producto(), "Humitas", "Comida", 1.50, disponible=True)
    )
    restaurante.registrar_producto(
        Producto(restaurante.generar_codigo_producto(), "Jugo de tomate", "Bebida", 1.50, disponible=True)
    )
    restaurante.registrar_usuario(
        Usuario("1101234567", "Danny Betancourt", "danny@correo.com")
    )
    restaurante.registrar_usuario(
        Usuario("1107654321", "Carlos Pérez", "carlos@correo.com")
    )


def mostrar_menu() -> None:
    """Imprime el menu principal del sistema a partir de la tupla de opciones."""
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for linea in OPCIONES_MENU:
        print(linea)


def solicitar_float(mensaje: str) -> float:
    """Solicita un numero decimal al usuario validando la entrada."""
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Valor invalido. Ingrese un numero (ej: 4.50).")


def solicitar_bool(mensaje: str) -> bool:
    """Solicita una respuesta s/n al usuario y la convierte a booleano."""
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ("s", "si", "sí"):
            return True
        if valor in ("n", "no"):
            return False
        print("Valor invalido. Responda 's' o 'n'.")


def solicitar_float_opcional(mensaje: str) -> "float | None":
    """Solicita un numero decimal, permitiendo dejarlo vacio (Enter)."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        try:
            return float(valor)
        except ValueError:
            print("Valor invalido. Ingrese un numero o deje vacio para no modificar.")


def solicitar_bool_opcional(mensaje: str) -> "bool | None":
    """Solicita s/n, permitiendo dejarlo vacio (Enter) para no modificar."""
    while True:
        valor = input(mensaje).strip().lower()
        if valor == "":
            return None
        if valor in ("s", "si", "sí"):
            return True
        if valor in ("n", "no"):
            return False
        print("Valor invalido. Responda 's', 'n' o deje vacio para no modificar.")


def registrar_producto(restaurante: Restaurante) -> None:
    """Solicita los datos de un producto y lo registra en el servicio.

    
    """
    print("\n--- Registrar producto ---")
    nombre: str = input("Nombre: ").strip()
    categoria: str = input("Categoria: ").strip()
    precio: float = solicitar_float("Precio: ")
    disponible: bool = solicitar_bool("Disponible (s/n): ")

    codigo: str = restaurante.generar_codigo_producto()
    producto = Producto(codigo, nombre, categoria, precio, disponible)
    restaurante.registrar_producto(producto)
    print(f"Producto registrado correctamente con el código '{codigo}'.\n")


def buscar_producto(restaurante: Restaurante) -> None:
  
    print("\n--- Buscar producto ---")
    codigo: str = input("Código del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto is None:
        print(f"No existe un producto con el código '{codigo}'.\n")
        return
    print(producto.mostrar_informacion())
    print()


def actualizar_producto(restaurante: Restaurante) -> None:
  
    print("\n--- Actualizar producto ---")
    codigo: str = input("Código del producto a actualizar: ").strip()

    if restaurante.buscar_producto(codigo) is None:
        print(f"No existe un producto con el código '{codigo}'.\n")
        return

    print("Deje el campo vacío (Enter) para no modificarlo.")
    nombre: str = input("Nuevo nombre: ").strip()
    categoria: str = input("Nueva categoría: ").strip()
    precio = solicitar_float_opcional("Nuevo precio: ")
    disponible = solicitar_bool_opcional("Nueva disponibilidad (s/n): ")

    restaurante.actualizar_producto(
        codigo,
        nombre=nombre or None,
        categoria=categoria or None,
        precio=precio,
        disponible=disponible,
    )
    print("Producto actualizado correctamente.\n")


def eliminar_producto(restaurante: Restaurante) -> None:
    """Solicita un codigo y elimina el producto correspondiente."""
    print("\n--- Eliminar producto ---")
    codigo: str = input("Código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.\n")
    else:
        print(f"No existe un producto con el código '{codigo}'.\n")


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra en consola todos los productos registrados."""
    print("\nPRODUCTOS REGISTRADOS")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.\n")
        return
    for info in productos:
        print(info)
    print()


def registrar_usuario(restaurante: Restaurante) -> None:
    """Solicita los datos de un usuario y lo registra en el servicio."""
    print("\n--- Registrar usuario ---")
    identificacion: str = input("Identificación: ").strip()
    nombre: str = input("Nombre: ").strip()
    correo: str = input("Correo: ").strip()

    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.\n")
    else:
        print(f"Error: ya existe un usuario con la identificación '{identificacion}'.\n")


def listar_usuarios(restaurante: Restaurante) -> None:
    """Muestra en consola todos los usuarios registrados."""
    print("\nUSUARIOS REGISTRADOS")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return
    for info in usuarios:
        print(info)
    print()


def mostrar_categorias(restaurante: Restaurante) -> None:
    """Muestra las categorias unicas de los productos registrados."""
    print("\nCATEGORÍAS REGISTRADAS")
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.\n")
        return
    for categoria in sorted(categorias):
        print(f"- {categoria}")
    print()


def main() -> None:
    """Funcion principal que ejecuta el bucle del menu interactivo."""
    restaurante = Restaurante("Restaurante Sabor Lojano")
    cargar_datos_iniciales(restaurante)
    mostrar_encabezado(restaurante)

    # Diccionario: asocia cada opcion del menu (clave) con la funcion
    # que debe ejecutarse (valor), evitando una cadena extensa de
    # condicionales if/elif.
    opciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()
        opcion: str = input("Seleccione una opcion: ").strip()

        if opcion == "9":
            print("\nGracias por usar el Sistema de Restaurante. ¡Hasta pronto!")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("\nOpción inválida. Intente nuevamente.\n")
            continue

        try:
            accion(restaurante)
        except Exception as error:  # noqa: BLE001 - evita que el programa se detenga
            print(f"\nOcurrió un error inesperado al procesar la opción: {error}\n")


if __name__ == "__main__":
    main()
