"""Validaciones de datos de entrada para usuarios."""


class ValidacionError(Exception):
    """Excepción personalizada para errores de validación."""

    pass


def validar_nombre(nombre: str) -> str:
    """Valida que el nombre no esté vacío y tenga al menos 2 caracteres."""
    nombre = nombre.strip()
    if not nombre:
        raise ValidacionError("El nombre no puede estar vacío.")
    if len(nombre) < 2:
        raise ValidacionError("El nombre debe tener al menos 2 caracteres.")
    return nombre


def validar_edad(edad_str: str) -> int:
    """Valida que la edad sea un número entero entre 1 y 120."""
    try:
        edad = int(edad_str.strip())
    except ValueError as exc:
        raise ValidacionError("La edad debe ser un número entero válido.") from exc

    if edad < 1 or edad > 120:
        raise ValidacionError("La edad debe estar entre 1 y 120 años.")
    return edad


def validar_email(email: str) -> str:
    """Valida formato básico de correo electrónico."""
    email = email.strip()
    if not email:
        raise ValidacionError("El correo electrónico no puede estar vacío.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValidacionError("El correo electrónico no tiene un formato válido.")
    return email


def validar_usuario(nombre: str, edad_str: str, email: str) -> dict:
    """Valida todos los campos de un usuario y retorna un diccionario limpio."""
    return {
        "nombre": validar_nombre(nombre),
        "edad": validar_edad(edad_str),
        "email": validar_email(email),
    }
