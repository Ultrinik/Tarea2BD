# Informe Tarea 3 Bases de Datos 2021-1 Grupo 30
## Integrantes
- Nicolás Castro Espinosa - 201973025-8
- Benjamin Aros Baez 201730028-0
- Lucas Antoncich Loyola 201621012-1
 
## Supuestos y consideraciones:
 - Para actualizar y borrar "usuario_tiene_moneda" se debe introducir primero el id del usuario y luego el de la moneda, es decir para actualizar la moneda 8 del usuario 1, se usa la dirección "127.0.0.1:5000/api/usuario_tiene_moneda/1/8".
 - Para actualizar y borrar "precio_moneda" se debe introducir primero el id del usuario y luego la fecha (timestamp), es decir para actualizar la moneda 1 en la fecha 2020-07-29 22:22:09.368082, se usa la dirección "127.0.0.1:5000/api/precio_moneda/1/2020-07-29 22:22:09.368082".
 - Se requiere la librería "curl" de php, que se utilizó para realizar requests de tipo PUT y DELETE.
 - Para comunicarse con la api de flask (primeras 5 consultas) entregamos los siguientes ejemplos:
 
 1. curl -H "Content-Type: application/json" -X POST -d '{"year":"2017"}' http://127.0.0.1:5000/api/consultas/1
 
 2. curl -H "Content-Type: application/json" -X POST -d '{"min":"7000"}' http://127.0.0.1:5000/api/consultas/2
 
 3. curl -H "Content-Type: application/json" -X POST -d '{"pais":"Australia"}' http://127.0.0.1:5000/api/consultas/3
 
 4. curl -H "Content-Type: application/json" -X POST -d '{"coin":"Dogecoin"}' http://127.0.0.1:5000/api/consultas/4
 
 5. curl -H "Content-Type: application/json" -X POST -d '{"sigla":"XRP"}' http://127.0.0.1:5000/api/consultas/5
 
 
