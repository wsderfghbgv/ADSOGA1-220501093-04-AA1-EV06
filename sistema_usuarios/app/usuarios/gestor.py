"""Gestor de usuarios: registro, listado y búsquedas."""

from app.config.settings import ADMIN_USER
from app.usuarios.validaciones import ValidacionError, validar_usuario


class UsuarioDuplicadoError(Exception):
    """Excepción cuando se intenta registrar un usuario con email existente."""

    pass


class UsuarioNoEncontradoError(Exception):
    """Excepción cuando no se encuentra un usuario en la búsqueda."""

    pass


class GestorUsuarios:
    """Administra el registro, listado y búsqueda de usuarios."""

    def __init__(self) -> None:
        self._usuarios: list[dict] = []

    def registrar(self, nombre: str, edad_str: str, email: str) -> dict:
        """Registra un nuevo usuario tras validar sus datos."""
        datos = validar_usuario(nombre, edad_str, email)

        if any(u["email"].lower() == datos["email"].lower() for u in self._usuarios):
            raise UsuarioDuplicadoError(
                f"Ya existe un usuario con el correo '{datos['email']}'."
            )

        usuario = {
            "id": len(self._usuarios) + 1,
            "nombre": datos["nombre"],
            "edad": datos["edad"],
            "email": datos["email"],
            "rol": "admin" if datos["nombre"].lower() == ADMIN_USER.lower() else "usuario",
        }
        self._usuarios.append(usuario)
        return usuario

    def listar(self) -> list[dict]:
        """Retorna la lista completa de usuarios registrados."""
        return list(self._usuarios)

    def buscar_por_nombre(self, nombre: str) -> list[dict]:
        """Busca usuarios cuyo nombre contenga el texto indicado."""
        nombre = nombre.strip()
        if not nombre:
            raise ValidacionError("Debe ingresar un nombre para buscar.")

        resultados = [
            u for u in self._usuarios if nombre.lower() in u["nombre"].lower()
        ]
        if not resultados:
            raise UsuarioNoEncontradoError(
                f"No se encontraron usuarios con el nombre '{nombre}'."
            )
        return resultados

    def buscar_por_email(self, email: str) -> dict:
        """Busca un usuario por su correo electrónico exacto."""
        email = email.strip()
        if not email:
            raise ValidacionError("Debe ingresar un correo para buscar.")

        for usuario in self._usuarios:
            if usuario["email"].lower() == email.lower():
                return usuario

        raise UsuarioNoEncontradoError(
            f"No se encontró un usuario con el correo '{email}'."
        )

    @property
    def total(self) -> int:
        """Retorna la cantidad total de usuarios registrados."""
        return len(self._usuarios)
