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

_- Python 3.5.0:_ https://www.python.org/downloads/

_- Comando pip._

_- Django (última versión):_ https://www.djangoproject.com/

_- Sqlite 3:_ https://www.sqlite.org/index.html

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
4._Intalando Sqlite 3..._
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
3. _Creamos las migraciones correspondientes a las aplicaciones ejecutando:_
```
$ python manage.py makemigrations
```
📌 NOTA: Este comando creará la base de datos del proyecto.

4. _Ejecutamos las migraciones creadas:_
```
$ python manage.py migrate
```
5. _Creamos el superuser que nos permitirá acceder al administrador de Django en el proyecto:_
```
$ python manage.py superuser
```
6. _Introduzca las credenciales que desea para el administrador._

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

## Arquitectura 📖
El framework Django utiliza un patrón de arquitectura MTV (Model-Template-View), similar al conocido patrón MVC, por ello se decidió utilizar dicho patrón.

_El Modelo manipula los datos de la aplicación._
_El Template define cómo se mostrarán los datos en el navegador._
_La Vista decide qué datos mostrará el Template._

¿Cómo funciona?
1. El navegador hace una petición a una url, derivando en el envío de la petición a la Vista configurada.
2. La Vista, donde se encuentra programada la lógica de negocio, le hace la petición al Modelo solicitando o enviando datos.
3. El Modelo busca los datos solicitados o guarda los datos recibidos en la base de datos.
4. La base de datos responde al Modelo.
5. El Modelo manda la respuesta a la Vista.
6. La Vista envía los datos o respuesta al Template correspondiente.
7. El Template se renderiza en el navegador para ser mostrado.

Se utilizaron además servicios REST para las peticiones, siendo métodos utilizados GET y POST.
Para la base de datos se ha utilizado el motor Sqlite 3.

## Posibles mejoras 🛠️
- Las validaciones de los campos podrían mejorarse según la lógica del negocio y su ubicación geográfica. Ejemplo: Composición del CUIT en otro país distinto a la Argentina.
- Los valores de los select de Provincia y Responsable Inscripto podrían ser cargados en la base de datos para evitar ensuciar el código con arrays innecesarios.
- Podría permitirse que una dirección pertenezca a más de un proveedor, para contemplar familiares.
- Podría permitirse que los valores de ciertos campos permitan valores con acento y/o ñ. No ha sido posible en esta versión ya que, al toparse con este error, no se encontró una solución disponible para Python 3 al realizar la búsqueda de una solución en el tiempo estipulado para el proyecto. Se conoce que existía una sección de código que solucionaba este error para versiones de Python inferiores a 2.5, pero no era recomendable su uso ya que generaba conflictos a largo plazo.
- Debería aplicarse una baja lógica de los proveedores, no una baja física como se realiza actualmente. De esta forma, se mantendría un histórico en la base de datos.


## Autor/es ✒️

* **Hoz Aylen**
