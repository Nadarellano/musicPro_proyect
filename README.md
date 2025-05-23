### 🌐 MusicPro – Página web Instrumentos Musicales

MusicPro es una página web de ventas de instrumentos musicales con sistema de pago **transbank integrado**.

**Tecnologías utilizadas:**
- Django, JS, Bootstrap

---

Comando para instalar lib entorno virtual.

```shell
pip install virtualenv
```

Comando para crear un entorno virtual llamado env_musicP

```shell
virtualenv env_musicP
```

Comando para cargar entorno virtual en Windows (GitBash activar cada vez que se quiera trabajar en el proyecto)

```shell
. env_musicP/Scripts/activate
```

Instalar dependencia requests.

```shell
pip install Django
```

Crear archivo requirements.txt (Dependencias) ejecutar cada vez que hayan cambios para actualizar.

```shell
pip freeze > requirements.txt
```

Instalar dependencias a partir del archivo requirments.txt.

```shell
pip install -r requirements.txt
```

Comando para ejecutar aplicación

```shell
python manage.py runserver
```
Comando para desactivar el entorno virtual cada vez que se termine de trabajar en el proyecto

```shell
deactivate
```

Comando para instalar bootstrap5

```shell
pip install django-bootstrap5
```

Superuser and password (admin-Django)

```
music_pro
```

Instalar cors (Permite acceso de front-end React)
```shell
python -m pip install django-cors-headers / (https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework)
```


