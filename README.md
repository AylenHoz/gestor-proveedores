# Gestor de proveedores

_CRUD de proveedores con validaciones de campos. Desarrollado en Python/Django._

## Comenzando 🚀
1. _Abre la consola y posicionate en la carpeta donde desea que el proyecto se ubique._

2. _Ejecute el siguiente comando:_
```
$ git clone https://github.com/AylenHoz/gestor-proveedores.git
```

_No olvides cumplir con los pre-requisitos del proyecto._

Mira la sección de **Despliegue** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_- Python 3.5.0_

_- Comando pip._

_- Django (última versión)_

_- Sqlite3._

### Instalación en Ubuntu 🔧

1. _Instalando Python 3.5.0..._
```
$ wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
$ sudo tar xzf Python-3.5.0.tgz
$ cd Python-3.5.0
$ sudo ./configure --enable-optimizations
$ sudo apt install python-pip
```
2. _Instalando comando pip..._
```
$ sudo apt install python-pip
```
3. _Instalando Django..._
```
$ pip install django
```
Para conocer los paquetes instalados globalmente:
```
$ pip freeze
```
4._Intalando Sqlite3..._
```
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

## Despliegue 📦

_Desplegando el proyecto por primera vez:_
1. _Con la consola debemos pararnos sobre el directorio donde se encuentra el proyecto._

2. _Una vez allí:_
```
$ cd gestor-proveedores
```
6. _Creamos las migraciones correspondientes a las aplicaciones ejecutando:_
```
$ python manage.py makemigrations
```
NOTA: Este comando creará la base de datos del proyecto.

3. _Ejecutamos las migraciones creadas:_
```
$ python manage.py migrate
```
4. _Creamos el superuser que nos permitirá acceder al administrador de Django en el proyecto:_
```
$ python manage.py superuser
```
5. _Introduzca las credenciales que desea para el administrador._

7. _Finalmente, iniciamos el server:_
```
$ python manage.py runserver
```


_Si no es la primera vez..._
1. _Con la consola debemos pararnos sobre el directorio donde se encuentra el proyecto._

2. _Una vez allí:_
```
$ cd gestor-proveedores
```
3. _Ejecute:_
```
$ python manage.py runserver
```

## Ejecutando las pruebas ⚙️

1. _Con la consola debemos pararnos sobre el directorio donde se encuentra el proyecto._

2. _Una vez allí:_
```
$ cd gestor-proveedores
```
3. _Para ejecutar los test unitarios, ejecutar el siguiente comando:_
```
$ python manage.py test apps/proveedor
```
4. _Listo, ahora ¡Observa los resultados!_

## Autor/es ✒️

* **Hoz Aylen**
