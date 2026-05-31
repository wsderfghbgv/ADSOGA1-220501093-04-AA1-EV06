# Sistema Modular de Configuración y Gestión de Usuarios

**GA1-220501093-04-AA1-EV06** — Python avanzado: Entornos Virtuales, Gestión de Dependencias, Variables de Entorno y Modularización.

Aplicación de consola desarrollada en Python que permite registrar, listar y buscar usuarios, aplicando buenas prácticas de modularización, gestión de dependencias y configuración mediante variables de entorno.

---

## Requisitos previos

- Python 3.10 o superior
- Git
- Terminal de comandos (PowerShell, CMD o bash)
- Editor de código (Visual Studio Code recomendado)

---

## Estructura del proyecto

```
sistema_usuarios/
├── app/                        # Paquete principal de la aplicación
│   ├── __init__.py
│   ├── config/                 # Paquete de configuración
│   │   ├── __init__.py
│   │   └── settings.py         # Carga de variables de entorno
│   └── usuarios/               # Paquete de gestión de usuarios
│       ├── __init__.py
│       ├── gestor.py           # Registro, listado y búsquedas
│       └── validaciones.py     # Validaciones de datos de entrada
├── docs/
│   └── capturas/               # Carpeta para capturas de pantalla
├── venv/                       # Entorno virtual (no se sube a Git)
├── .env                        # Variables de entorno locales (no se sube a Git)
├── .env.example                # Plantilla de variables de entorno
├── .gitignore
├── main.py                     # Punto de entrada de la aplicación
├── requirements.txt            # Dependencias del proyecto
└── README.md
```

### Explicación de módulos y paquetes

| Elemento | Tipo | Responsabilidad |
|----------|------|-----------------|
| `app/` | Paquete | Contenedor principal de la lógica de la aplicación |
| `app/config/` | Subpaquete | Gestión de configuración y variables de entorno |
| `app/config/settings.py` | Módulo | Carga `.env` con `python-dotenv` y expone `APP_NAME`, `APP_VERSION`, `ADMIN_USER` |
| `app/usuarios/` | Subpaquete | Lógica de negocio relacionada con usuarios |
| `app/usuarios/validaciones.py` | Módulo | Valida nombre, edad y correo; lanza `ValidacionError` |
| `app/usuarios/gestor.py` | Módulo | Registra, lista y busca usuarios en memoria |
| `main.py` | Módulo | Menú interactivo de consola; punto de entrada |

**Modularización:** cada archivo tiene una responsabilidad única. `main.py` solo coordina la interfaz; `gestor.py` maneja los datos; `validaciones.py` centraliza las reglas de validación; `settings.py` aísla la configuración del resto del código.

---

## Fase 1 — Configuración del entorno virtual

### Crear el entorno virtual con `venv`

```powershell
# Windows (PowerShell)
cd sistema_usuarios
python -m venv venv
```

```bash
# Linux / macOS
cd sistema_usuarios
python3 -m venv venv
```

> **Captura de pantalla:** guardar en `docs/capturas/01_creacion_entorno_virtual.png`

### Activar el entorno virtual

```powershell
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

```cmd
# Windows (CMD)
venv\Scripts\activate.bat
```

```bash
# Linux / macOS
source venv/bin/activate
```

Cuando el entorno está activo, verás `(venv)` al inicio de la línea de la terminal.

---

## Fase 2 — Instalación de dependencias

### Con pip

```powershell
pip install -r requirements.txt
```

O instalar directamente:

```powershell
pip install python-dotenv
```

### Con uv (gestor moderno de dependencias)

```powershell
# Instalar uv (si no lo tienes)
pip install uv

# Instalar dependencias
uv pip install -r requirements.txt
```

> **Captura de pantalla:** guardar en `docs/capturas/02_instalacion_dependencias.png`

### Generar `requirements.txt`

```powershell
pip freeze > requirements.txt
```

Contenido actual:

```
python-dotenv==1.2.2
```

---

## Fase 3 — Variables de entorno

1. Copia el archivo de ejemplo:

```powershell
copy .env.example .env
```

2. Edita `.env` con tus valores:

```env
APP_NAME=Sistema Usuarios
APP_VERSION=1.0
ADMIN_USER=admin
```

3. Las variables se cargan automáticamente en `app/config/settings.py` usando `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "Sistema Usuarios")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
```

> **Uso seguro:** nunca subas `.env` a GitHub. Usa `.env.example` como plantilla sin datos sensibles. El archivo `.env` está incluido en `.gitignore`.

> **Captura de pantalla:** guardar en `docs/capturas/04_variables_entorno.png`

---

## Fase 4 — Ejecutar el proyecto

Con el entorno virtual activado:

```powershell
python main.py
```

### Menú disponible

| Opción | Acción |
|--------|--------|
| 1 | Registrar usuario (nombre, edad, correo) |
| 2 | Listar todos los usuarios |
| 3 | Buscar usuarios por nombre |
| 4 | Buscar usuario por correo |
| 5 | Salir |

### Funcionalidades implementadas

- Registro de usuarios con validación de datos
- Listado de usuarios registrados
- Búsqueda por nombre (coincidencia parcial)
- Búsqueda por correo (coincidencia exacta)
- Mensajes personalizados usando `APP_NAME` y `APP_VERSION`
- Asignación automática de rol `admin` si el nombre coincide con `ADMIN_USER`
- Manejo de errores con excepciones personalizadas:
  - `ValidacionError` — datos inválidos
  - `UsuarioDuplicadoError` — correo ya registrado
  - `UsuarioNoEncontradoError` — búsqueda sin resultados

> **Captura de pantalla:** guardar en `docs/capturas/03_ejecucion_sistema.png`

---



---


## Evidencias de aprendizaje

Repositorio en GitHub con:

- [x] Proyecto funcional
- [x] Entorno virtual configurado (`venv/`)
- [x] `requirements.txt`
- [x] `.env.example`
- [x] `README.md` documentado

---

## Autor

Aprendiz — GA1-220501093-04-AA1-EV06  
SENA — Análisis y Desarrollo de Software
