# Web-Movies
Proyecto en Django Web de películas con deploy en Azure
----------------------------------------------------------

Lo primero

Creamos un entorno virtual.

```
$ python -m venv env
```
Tenemos que activar nuestro entorno virtual, tendremos que desplzarnos a la carpeta scripts.
```
$ cd env/scripts
```
Activamos nuestro entorno virtual.
```
$ .\activate
```
Ya tendriamos antivado nuestro entorno virtual, debería salirte a la izquiera en color verde (env), eso quiere decir que esta activado ya.

Ahora tenemos que regresar a nuestra carpeta del archivo para eso utilizamos el siguiente comando por dos veces para regresar.

```
$ cd .. 
```

Ahora pasaremos a instalar las dependencias del proyecto.
```
$ pip install -r requirements.txt
```

Por último ya solo te queda hacer las migraciones.
```
$ python manage.py makemigrations
```
```
$ python manage.py migarate
```
```
$ python manage.py runserver
```

Para poder aregar nuevas películas o artículos tengras que crearte un usuario. Rellena los datos que te pide, como nombre de usuario, 
el email lo puedes dejar en blanco si quieres dandole a enter y por último introduce una contraseña y repitela.
```
$ python manage.py createsuperuser
```

Espero que os guste mi proyecto.
Cualquier sugerencia o participación que quieras aportar es bienvenida.



