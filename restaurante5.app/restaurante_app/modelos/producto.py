"""Modulo que contiene la clase Producto."""


class Producto:
    """Representa un producto del restaurante.

    El codigo se genera automaticamente desde el servicio Restaurante,
    por lo que no se solicita manualmente al usuario.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool = True,
    ) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio
        self.disponible: bool = disponible

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la informacion del producto."""
        return (
            f"Código: {self.codigo} | Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Disponible: {self.disponible}"
        )
