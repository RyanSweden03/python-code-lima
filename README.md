## Instalación y configuración

Sigue estos pasos para ejecutar el proyecto localmente:

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

```
### 2. Crear y activar el entorno virtual (opcional)
```
python3 -m venv venv

venv\Scripts\activate
```

### 3. Instalar dependencias
```
pip install -r requirements.txt
```

### 4. Configurar la base de datos MySQL
Crea una base de datos llamada employee_db en MySQL

```
CREATE DATABASE employee_db;
```
### 5. Actualiza el archivo config.py con tus credenciales de MySQL:

``` python
DATABASE_CONFIG = {
    'user': 'root',          
    'password': 'your_password',
    'host': 'localhost',        
    'database': 'employee_db'   
}
```

### 6.  Ejecutar la aplicación
```bash
python app.py

Una vez que Flask esté ejecutándose, dirigirse a:
http://localhost:5000/

```




