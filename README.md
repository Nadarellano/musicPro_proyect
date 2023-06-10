# musicPro_proyect
Prueba3 / Examen "Integración de Plataformas"

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