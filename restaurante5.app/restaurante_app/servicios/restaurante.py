"""Modulo que contiene la clase de servicio Restaurante."""

from typing import Dict, List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios.

    Aplica varias estructuras de datos de Python, cada una con una
    finalidad concreta dentro del sistema:

    - list: `self._productos` y `self._usuarios` mantienen las
      colecciones dinamicas de objetos que se registran, listan,
      actualizan y eliminan durante la ejecucion.
    - dict: `self._indice_productos` asocia cada codigo de producto
      (clave) con su objeto Producto (valor), permitiendo busquedas,
      actualizaciones y eliminaciones eficientes sin recorrer toda la
      lista cada vez.
    - set: `obtener_categorias()` recorre los productos registrados y
      devuelve un conjunto con las categorias unicas, sin duplicados.
    """

    def __init__(self, nombre: str = "Restaurante Sabor Lojano") -> None:
        self.nombre: str = nombre
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._indice_productos: Dict[str, Producto] = {}
        self._contador_producto: int = 0

    # ---------------------- Gestion de productos ----------------------

    def generar_codigo_producto(self) -> str:
        """Genera automaticamente el siguiente codigo de producto."""
        self._contador_producto += 1
        return str(self._contador_producto)

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su codigo no esta repetido.

        Devuelve True si el registro fue exitoso, False si el codigo
        ya existia.
        """
        if producto.codigo in self._indice_productos:
            return False
        self._productos.append(producto)
        self._indice_productos[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su codigo. Devuelve None si no existe."""
        return self._indice_productos.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
        disponible: Optional[bool] = None,
    ) -> bool:
        """Actualiza los campos indicados de un producto existente.

        Solo se modifican los campos que se reciban distintos de None,
        lo que permite actualizaciones parciales. Devuelve True si el
        producto existe y fue actualizado, False si no se encontro.
        """
        producto = self._indice_productos.get(codigo)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        if disponible is not None:
            producto.disponible = disponible
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su codigo.

        Devuelve True si el producto existia y fue eliminado, False si
        no se encontro.
        """
        producto = self._indice_productos.pop(codigo, None)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def listar_productos(self) -> List[str]:
        """Devuelve la informacion de todos los productos registrados."""
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_categorias(self) -> Set[str]:
        """Devuelve el conjunto de categorias unicas de los productos.

        Se utiliza un set para eliminar automaticamente las categorias
        repetidas entre los distintos productos registrados.
        """
        return {producto.categoria for producto in self._productos}

    # ----------------------- Gestion de usuarios -----------------------

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario si su identificacion no esta repetida.

        Devuelve True si el registro fue exitoso, False si la
        identificacion ya existia.
        """
        if self._buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[str]:
        """Devuelve la informacion de todos los usuarios registrados."""
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    def _buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None
