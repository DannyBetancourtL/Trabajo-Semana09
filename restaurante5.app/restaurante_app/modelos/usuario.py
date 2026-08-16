"""Modulo que contiene la clase Usuario."""


class Usuario:
    """Representa de forma general a una persona registrada en el sistema.

    Esta clase concentra la informacion basica de cualquier persona
    registrada (identificacion, nombre y correo), sin definir todavia
    una jerarquia de tipos especificos de usuario (cliente, empleado,
    administrador, etc.). Esa especializacion se abordara en una
    actividad posterior.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la informacion del usuario."""
        return (
            f"Identificación: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
