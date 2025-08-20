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
