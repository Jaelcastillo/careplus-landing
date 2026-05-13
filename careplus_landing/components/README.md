# CarePlus Landing Page - Reflex + Poetry

## Descripción del Proyecto

Este proyecto consiste en la recreación de una landing page médica profesional utilizando:

* Python
* Reflex
* Poetry
* Visual Studio Code
* GitHub

El objetivo del proyecto es aplicar conocimientos de desarrollo frontend utilizando Reflex para construir una interfaz moderna, organizada y responsive.

---

# Tecnologías Utilizadas

| Tecnología         | Uso                        |
| ------------------ | -------------------------- |
| Python 3.12        | Lenguaje principal         |
| Reflex             | Framework frontend/backend |
| Poetry             | Gestión de dependencias    |
| Git                | Control de versiones       |
| GitHub             | Repositorio remoto         |
| Visual Studio Code | Editor de código           |

---

# Requisitos Previos

Antes de ejecutar el proyecto, la computadora debe tener instalado:

## 1. Python 3.12

Verificar instalación:

```powershell
py -3.12 --version
```

Debe mostrar algo parecido a:

```txt
Python 3.12.x
```

---

## 2. Poetry

Verificar instalación:

```powershell
poetry --version
```

Debe mostrar:

```txt
Poetry (version 2.x.x)
```

---

## 3. Node.js

Verificar instalación:

```powershell
node -v
```

y:

```powershell
npm -v
```

---

## 4. Git

Verificar instalación:

```powershell
git --version
```

---

## 5. Visual Studio Code

Abrir desde terminal:

```powershell
code .
```

---

# Clonar el Proyecto

## 1. Abrir PowerShell

## 2. Moverse a la carpeta deseada

Ejemplo:

```powershell
cd C:\Users\Usuario\Desktop
```

---

## 3. Clonar el repositorio

```powershell
git clone https://github.com/Jaelcastillo/careplus-landing.git
```

---

## 4. Entrar a la carpeta del proyecto

```powershell
cd careplus-landing
```

---

# Configuración del Entorno Virtual

## 1. Configurar Python 3.12

Ejecutar:

```powershell
poetry env use "C:\Users\USUARIO\AppData\Local\Programs\Python\Python312\python.exe"
```

NOTA:

La ruta puede cambiar dependiendo de la computadora.

Para encontrar la ruta correcta:

```powershell
py -3.12 -c "import sys; print(sys.executable)"
```

---

## 2. Instalar dependencias

```powershell
poetry install
```

Esto instalará automáticamente:

* Reflex
* Dependencias del proyecto
* Librerías necesarias

---

# Ejecutar el Proyecto

## 1. Ejecutar la aplicación

```powershell
poetry run reflex run
```

---

## 2. Abrir en navegador

Abrir:

```txt
http://localhost:3000
```

---

# Estructura del Proyecto

```txt
careplus-landing/
│
├── assets/
│   ├── doctor.png
│   ├── diagnostics.jpg
│   ├── surgery.jpg
│   └── pharmacy.jpg
│
├── careplus_landing/
│   ├── components/
│   │   ├── navbar.py
│   │   ├── hero.py
│   │   ├── departments.py
│   │   └── services.py
│   │
│   ├── __init__.py
│   └── careplus_landing.py
│
├── .gitignore
├── pyproject.toml
├── rxconfig.py
└── README.md
```

---

# Explicación de Componentes

## 1. Navbar

Archivo:

```txt
components/navbar.py
```

Contiene:

* Logo
* Menú de navegación
* Botón de cita médica

---

## 2. Hero Section

Archivo:

```txt
components/hero.py
```

Contiene:

* Título principal
* Imagen médica
* Formulario de citas
* Fondo principal

---

## 3. Departments

Archivo:

```txt
components/departments.py
```

Contiene:

* Tarjetas médicas
* Categorías de departamentos
* Íconos SVG personalizados

---

## 4. Services

Archivo:

```txt
components/services.py
```

Contiene:

* Tarjetas de servicios destacados
* Imágenes
* Descripciones

---

# Comandos Importantes

## Ejecutar proyecto

```powershell
poetry run reflex run
```

---

## Instalar nuevas dependencias

```powershell
poetry add nombre_paquete
```

---

## Ver entorno virtual

```powershell
poetry env info
```

---

## Abrir Visual Studio Code

```powershell
code .
```

---

# Configuración Recomendada en VS Code

## Seleccionar intérprete Python

1. Presionar:

```txt
CTRL + SHIFT + P
```

2. Buscar:

```txt
Python: Select Interpreter
```

3. Seleccionar:

```txt
careplus-landing/.venv
```

---

# Configuración Completa del Proyecto Desde Cero

Esta guía permite que cualquier persona con una computadora y los programas instalados pueda ejecutar correctamente el proyecto.

---

# PASO 1 - Abrir PowerShell

Abrir PowerShell como usuario normal.

---

# PASO 2 - Clonar el repositorio

Ejecutar:

```powershell
git clone https://github.com/Jaelcastillo/careplus-landing.git
```

---

# PASO 3 - Entrar al proyecto

```powershell
cd careplus-landing
```

---

# PASO 4 - Abrir Visual Studio Code

IMPORTANTE:

El proyecto debe abrirse desde la carpeta raíz utilizando:

```powershell
code .
```

El punto final es obligatorio porque indica que se abrirá la carpeta actual.

---

# PASO 5 - Verificar Python

Verificar que Python 3.12 esté instalado:

```powershell
py -3.12 --version
```

Debe mostrar:

```txt
Python 3.12.x
```

---

# PASO 6 - Obtener ruta de Python

Ejecutar:

```powershell
py -3.12 -c "import sys; print(sys.executable)"
```

Ejemplo de salida:

```txt
C:\Users\Usuario\AppData\Local\Programs\Python\Python312\python.exe
```

---

# PASO 7 - Configurar entorno virtual con Poetry

Usar la ruta obtenida anteriormente:

```powershell
poetry env use "C:\Users\Usuario\AppData\Local\Programs\Python\Python312\python.exe"
```

---

# PASO 8 - Instalar dependencias

```powershell
poetry install
```

---

# PASO 9 - Ejecutar el proyecto

```powershell
poetry run reflex run
```

---

# PASO 10 - Abrir el navegador

Abrir:

```txt
http://localhost:3000
```

---

# Estructura Oficial del Proyecto

```txt
careplus-landing/
│
├── assets/
│   ├── doctor.png
│   ├── diagnostics.jpg
│   ├── surgery.jpg
│   └── pharmacy.jpg
│
├── careplus_landing/
│   ├── components/
│   │   ├── navbar.py
│   │   ├── hero.py
│   │   ├── departments.py
│   │   └── services.py
│   │
│   ├── __init__.py
│   └── careplus_landing.py
│
├── .gitignore
├── pyproject.toml
├── rxconfig.py
└── README.md
```

---

# Organización del Código

## careplus_landing.py

Archivo principal de la aplicación.

## navbar.py

Contiene el menú principal y navegación.

## hero.py

Contiene la sección principal y formulario.

## departments.py

Contiene las tarjetas médicas y categorías.

## services.py

Contiene las tarjetas de servicios destacados.

---

# Configuración Recomendada en VS Code

1. Presionar:

```txt
CTRL + SHIFT + P
```

2. Buscar:

```txt
Python: Select Interpreter
```

3. Seleccionar:

```txt
careplus-landing/.venv
```

---

# Comandos Importantes

```powershell
poetry run reflex run
```

```powershell
poetry install
```

```powershell
poetry add nombre_paquete
```

```powershell
poetry env info
```

```powershell
code .
```

---

# Buenas Prácticas Aplicadas

* separación por componentes
* arquitectura organizada
* uso de Reflex
* uso de Poetry
* control de versiones con Git
* diseño responsive
* reutilización de componentes
* estructura profesional

---

# Solución de Problemas

## Error: poetry no reconocido

Instalar Poetry nuevamente.

---

## Error: reflex no reconocido

Usar:

```powershell
poetry run reflex run
```

---

## Error: Cannot connect to websocket

Reiniciar Reflex:

```powershell
CTRL + C
```

Luego:

```powershell
poetry run reflex run
```

---

## Error: spacing inválido

Reflex solo acepta spacing entre:

```txt
0 a 9
```

Ejemplo correcto:

```python
spacing="8"
```

---

## Error: import cannot import name

Verificar que la función exista con el mismo nombre.

Ejemplo:

```python
def hero_section():
```

---

# Flujo de Trabajo con Git

## Verificar cambios

```powershell
git status
```

---

## Agregar cambios

```powershell
git add .
```

---

## Crear commit

```powershell
git commit -m "mensaje"
```

---

## Subir cambios

```powershell
git push
```

---

# Commits Realizados

```txt
Initial project setup
Initialize Reflex project
Crear barra de navegación y sección principal
Agregar secciones de departamentos y servicios
```

---

# Diseño Implementado

La landing page incluye:

* Navbar moderna
* Hero section médica
* Formulario de citas
* Tarjetas de departamentos
* Servicios destacados
* Diseño responsive
* Componentes reutilizables
* Organización profesional

---

# Autor

Jael Castillo

GitHub:

[https://github.com/Jaelcastillo](https://github.com/Jaelcastillo)

Repositorio:

[https://github.com/Jaelcastillo/careplus-landing](https://github.com/Jaelcastillo/careplus-landing)
