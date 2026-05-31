"""Punto de entrada del Sistema Modular de Configuración y Gestión de Usuarios."""

from app.config.settings import APP_NAME, APP_VERSION
from app.usuarios.gestor import (
    GestorUsuarios,
    UsuarioDuplicadoError,
    UsuarioNoEncontradoError,
)
from app.usuarios.validaciones import ValidacionError


def mostrar_encabezado() -> None:
    """Muestra el encabezado personalizado con variables de entorno."""
    print("=" * 50)
    print(f"  {APP_NAME} v{APP_VERSION}")
    print("=" * 50)


def mostrar_menu() -> None:
    """Muestra el menú principal de opciones."""
    print("\n--- Menú Principal ---")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar por nombre")
    print("4. Buscar por correo")
    print("5. Salir")


def mostrar_usuario(usuario: dict) -> None:
    """Muestra los datos de un usuario en formato legible."""
    print(f"  ID:     {usuario['id']}")
    print(f"  Nombre: {usuario['nombre']}")
    print(f"  Edad:   {usuario['edad']}")
    print(f"  Email:  {usuario['email']}")
    print(f"  Rol:    {usuario['rol']}")
    print("-" * 30)


def registrar_usuario(gestor: GestorUsuarios) -> None:
    """Solicita datos y registra un nuevo usuario."""
    print("\n--- Registrar Usuario ---")
    try:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        email = input("Correo electrónico: ")

        usuario = gestor.registrar(nombre, edad, email)
        print(f"\n[OK] Usuario '{usuario['nombre']}' registrado exitosamente.")
        print(f"  Rol asignado: {usuario['rol']}")
    except ValidacionError as e:
        print(f"\n[ERROR] Error de validacion: {e}")
    except UsuarioDuplicadoError as e:
        print(f"\n[ERROR] {e}")


def listar_usuarios(gestor: GestorUsuarios) -> None:
    """Lista todos los usuarios registrados."""
    print("\n--- Listado de Usuarios ---")
    usuarios = gestor.listar()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print(f"Total de usuarios: {gestor.total}\n")
    for usuario in usuarios:
        mostrar_usuario(usuario)


def buscar_por_nombre(gestor: GestorUsuarios) -> None:
    """Busca usuarios por nombre."""
    print("\n--- Buscar por Nombre ---")
    try:
        nombre = input("Ingrese el nombre a buscar: ")
        resultados = gestor.buscar_por_nombre(nombre)
        print(f"\nSe encontraron {len(resultados)} usuario(s):\n")
        for usuario in resultados:
            mostrar_usuario(usuario)
    except ValidacionError as e:
        print(f"\n[ERROR] Error de validacion: {e}")
    except UsuarioNoEncontradoError as e:
        print(f"\n[ERROR] {e}")


def buscar_por_email(gestor: GestorUsuarios) -> None:
    """Busca un usuario por correo electrónico."""
    print("\n--- Buscar por Correo ---")
    try:
        email = input("Ingrese el correo a buscar: ")
        usuario = gestor.buscar_por_email(email)
        print("\nUsuario encontrado:\n")
        mostrar_usuario(usuario)
    except ValidacionError as e:
        print(f"\n[ERROR] Error de validacion: {e}")
    except UsuarioNoEncontradoError as e:
        print(f"\n[ERROR] {e}")


def main() -> None:
    """Función principal que ejecuta el menú interactivo."""
    mostrar_encabezado()
    gestor = GestorUsuarios()

    opciones = {
        "1": registrar_usuario,
        "2": listar_usuarios,
        "3": buscar_por_nombre,
        "4": buscar_por_email,
    }

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "5":
            print(f"\nGracias por usar {APP_NAME}. ¡Hasta pronto!")
            break

        accion = opciones.get(opcion)
        if accion:
            accion(gestor)
        else:
            print("\n[ERROR] Opcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    main()
