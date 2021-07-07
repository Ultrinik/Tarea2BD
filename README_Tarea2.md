# Informe Tarea 2 Bases de Datos 2021-1 Grupo 30
## Integrantes
- Nicolás Castro Espinosa - 201973025-8
- Benjamin Aros Baez 201730028-0
- Lucas Antoncich Loyola 201621012-1
 
## Supuestos y consideraciones:
 - Consideramos, para el acceso como Administrador, las credenciales: correo = "admin@admin", contraseña: "123" (sin las comillas dobles).
 - Consideramos que, luego de tener un registro exitoso, el usuario no queda logeado en la página inmediatamente con las credenciales recién creadas, sino que es redirigido al login para introducir sus credenciales.


## Archivos adicionales:
### Imágenes:
- Se añadieron las imagenes img/fondo0.jpg, img/fondo1.jpg, img/fondo2.jpg, img/fondo3.jpg, con el objetivo de usarlas como fondo de pantalla en algunas vistas.
- Se añadieron las imagenes img/bitcoin.png, img/cheem.png, img/doge.png, con el objetivo de usarlas de manera complementaria en algunas vistas.

### HTML’s:
- Se añadió el html extras/redirect.html con el objetivo de informar al usuario al acceder a una vista sin permisos.
- Se añadió el html extras/sing-up-succes.html con el objeto de informar al usuario que su usuario ha sido creado con éxito.


## Modelo de datos:
### Usuario Admin:
Para implementar esto hemos añadido una columna booleana extra a la tabla usuario, llamada administrador.  
Ventajas: Una solución rápida y simple para categorizar.  
Desventajas: Se tuvo que actualizar a todos los otros usuarios en la DB con un valor para este nuevo atributo.

### Contraseñas de usuarios:
Se extendió el máximo de caracteres de las contraseñas a 60 caracteres para permitir el hashing de estas.  
Ventajas: Mayor seguridad para los usuarios.  
Desventajas: Ligero aumento de cómputo por los hasheos.

### Correo de usuarios:
El atributo correo pasa a ser único, ya que este es el dato que se usará para definir los registros.  
Ventajas: Evita tener que verificar en php si el correo está repetido en el login.  
Desventajas: Ninguna.

## Dificultades:
Nuestra principal dificultad en esta tarea consistió en el uso conjunto de las herramientas PHP, html y SQL, sumado a nuestros archivos, pues había que tomar en cuenta muchos cambios pequeños en cada archivo. Además, debido a que algunos integrantes del grupo poseían muy poca o nula experiencia trabajando con estos, se gastó bastante tiempo en aprender los conceptos básicos. Por suerte, estos lenguajes se encuentran bastante documentados y el uso de la biblia stack-overflow nos salvó varias veces. Esto aparte de las milenarias batallas contra los instaladores y configuraciones de las aplicaciones a utilizar, en las cuales vencimos luego de sangre sudor y lágrimas.

En términos de tiempo, estimamos que la tarea nos tomó un total de 30 horas entre los tres integrantes. Consideramos que gastamos la mayor parte del tiempo instalando y aprendiendo a usar PHP y HTML. 
