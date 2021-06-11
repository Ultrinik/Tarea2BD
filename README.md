# Informe Tarea 2 Bases de Datos 2021-1 Grupo 30
## Integrantes
- Nicolás Castro Espinosa - 201973025-8
- Benjamin Aros Baez 201730028-0
- Lucas Antoncich Loyola 201621012-1
 
## Supuestos y consideraciones:
blablabla

## Archivos adicionales:
### Imágenes:
- Se añadió la imagen img/bitcoin1.jpg con el objetivo de usarla como fondo de pantalla en algunas vistas.

### HTML’s:
- Se añadió el html extras/redirect.html con el objetivo de informar al usuario al acceder a una vista sin permisos.
- Se añadió el html extras/sing-up-succes.html con el objeto de informar al usuario que su usuario ha sido creado con éxito.

### PHP’s:
- blablabla

## Modelo de datos:
### Usuario Admin:
Para implementar esto hemos añadido una columna booleana extra a la tabla usuario, llamada administrador.
Ventajas: Una solución rápida y simple para categorizar.
Desventajas: Se tuvo que actualizar a todos los otros usuarios en la DB con un valor para este nuevo atributo.

### Contraseñas de usuario:
Se extendió el máximo de caracteres de las contraseñas a 60 caracteres para permitir el hashing de estas.
Ventajas: Mayor seguridad para los usuarios.
Desventajas: Ligero aumento de cómputo por los hasheos.

### Correo de usuarios:
El atributo correo pasa a ser único, ya que este es el dato que se usará para definir los registros.
Ventajas: Evita tener que verificar en php si el correo ya se registró.
Desventajas: No sé.

## Cambios extras a archivos:
blablabla

## Dificultades:
blablabla
