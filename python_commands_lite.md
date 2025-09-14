# Comandos básicos de Python venv y pip

Este archivo contiene los comandos más usados para trabajar con ambientes virtuales en Python usando `venv` y la gestión de paquetes con `pip`. Puedes agregar más comandos y secciones según tus necesidades.

---

## 1. Crear un entorno virtual
**Comando:**
```bash
python -m venv nombre_del_entorno
```
**Descripción:** Crea un nuevo ambiente virtual en la carpeta indicada.
**¿Para qué sirve?** Para aislar dependencias de proyectos Python.

---

## 2. Activar el entorno virtual
**Comando (Windows):**
```bash
nombre_del_entorno\Scripts\activate
```
**Comando (Linux/Mac):**
```bash
source nombre_del_entorno/bin/activate
```
**Descripción:** Activa el entorno virtual para instalar y usar paquetes solo ahí.
**¿Para qué sirve?** Para trabajar dentro del ambiente virtual.

---

## 3. Desactivar el entorno virtual
**Comando:**
```bash
deactivate
```
**Descripción:** Desactiva el entorno virtual y vuelve al entorno global.
**¿Para qué sirve?** Para salir del ambiente virtual.

---

## 4. Instalar paquetes dentro del entorno
**Comando:**
```bash
pip install nombre_paquete
```
**Descripción:** Instala un paquete en el entorno virtual activo.
**¿Para qué sirve?** Para agregar dependencias a tu proyecto.

---

## 5. Ver paquetes instalados
**Comando:**
```bash
pip list
```
**Descripción:** Muestra todos los paquetes instalados en el entorno virtual.
**¿Para qué sirve?** Para revisar dependencias instaladas.

---

## 6. Guardar dependencias en un archivo
**Comando:**
```bash
pip freeze > requirements.txt
```
**Descripción:** Guarda la lista de paquetes instalados en un archivo.
**¿Para qué sirve?** Para compartir dependencias con otros o para despliegue.

---

## 7. Instalar dependencias desde un archivo
**Comando:**
```bash
pip install -r requirements.txt
```
**Descripción:** Instala todos los paquetes listados en `requirements.txt`.
**¿Para qué sirve?** Para replicar el entorno en otra máquina.

---

## 8. Uso de archivos `.env` en proyectos Python

Los archivos `.env` permiten guardar variables de entorno sensibles (como contraseñas, claves API, configuraciones) fuera del código fuente.

### ¿Cómo crear un archivo `.env`?
**Comando:**
```bash
touch .env
```
O simplemente crea un archivo llamado `.env` en la raíz de tu proyecto.

### ¿Cómo escribir variables en `.env`?
Agrega líneas en el archivo con el formato:
```
NOMBRE_VARIABLE=valor
```

### ¿Cómo cargar variables de `.env` en Python?
Instala la librería `python-dotenv`:
```bash
pip install python-dotenv
```
En tu código Python:
```python
from dotenv import load_dotenv
load_dotenv()
```
Luego puedes acceder a las variables usando `os.getenv`:
```python
import os
valor = os.getenv("NOMBRE_VARIABLE")
```

### ¿Para qué sirve?
- Mantener configuraciones sensibles fuera del código.
- Facilitar el cambio de configuraciones sin modificar el código fuente.
- Mejorar la seguridad y portabilidad del proyecto.

### Recomendaciones
- No subir el archivo `.env` a repositorios públicos (agrega `.env` a tu `.gitignore`).
- Usa variables descriptivas y documenta su uso.

---

## 9. Comandos básicos para trabajar con MCP (Model Context Protocol)

### ¿Qué es MCP?

MCP (Model Context Protocol) es un estándar abierto y de código abierto para estandarizar la forma en que los sistemas de inteligencia artificial, como los modelos de lenguaje grandes (LLMs), intercambian contexto, instrucciones y resultados. MCP facilita la interoperabilidad entre diferentes modelos, agentes y aplicaciones, permitiendo una integración más sencilla y flexible en sistemas de IA.

### ¿Para qué sirve MCP?
- Permite que diferentes modelos y agentes de IA se comuniquen usando un formato común.
- Facilita la integración de LLMs en aplicaciones, flujos de trabajo y sistemas distribuidos.
- Estandariza el intercambio de contexto, instrucciones y resultados entre componentes de IA.

### Paquetes necesarios para MCP en Python

Para trabajar con MCP en Python, puedes usar el paquete oficial:

- **"mcp[cli]"** (referencia al SDK MCP con el componente de interfaz de línea de comandos (CLI) instalado.)
- REVISAR **mcp** (protocolo y utilidades MCP)
- **requests** (opcional, para comunicación HTTP)
- **python-dotenv** (opcional, para variables de entorno)

**Instalación:**
```bash
pip install "mcp[cli]"
```
```bash
pip install mcp requests python-dotenv
```

### Ejemplo básico de uso de MCP en Python

**Enviar contexto e instrucciones a un modelo MCP:**
```python
from mcp import Client

client = Client("http://localhost:8000")
context = {"user": "Juan", "task": "resumir texto"}
instructions = "Resume el siguiente texto en español."

response = client.send(context=context, instructions=instructions)
print("Respuesta del modelo:", response)
```

### Comandos para ejecución
**Ejecutar el servidor en modo desarrollo:**
```bash
mcp dev server.py
```
- este comando en consola muestra una url
- la url abre e l inspector
- si no funciona usa el siguiente comando -> npx @modelcontextprotocol/inspector mcp run server-py
- en la pagina en el momento hay que configurar si no estas usan uv lo siguiente
    - en command poner mcp
    - en Arguments poner run server-py
- listo conectar


### Recomendaciones

- Consulta la documentación oficial de MCP: https://github.com/modelcontext/modelcontext
- Usa variables de entorno para configurar endpoints y claves API.
- MCP puede usarse con modelos locales o servicios en la nube compatibles.

---

## Cómo agregar más comandos
Agrega una nueva sección siguiendo el formato:

### Título del comando
**Comando:**
```bash
comando_aqui
```
**Descripción:** Explica qué hace el comando.
**¿Para qué sirve?** Explica el uso práctico.

---

¡Usa este archivo como referencia rápida para ahorrar tiempo y recursos!

