from datetime import date, datetime, timedelta
import random as r

#Librerías para PostgreSQL
import pg
import psycopg2

usuario = "Escribir usuario"
nombreDB = "Escribir nombre BD"
contraseña = "Escribir contraseña"

connection = psycopg2.connect(
   host="localhost",
   user=usuario,
   dbname=nombreDB,
   password=contraseña
)

print(connection)
cursor = connection.cursor()

#Recuerde haber ejecutado todas las celdas anteriores!
print("Borrando Datos Antiguos...")
connection.commit() #en caso de algun error
query = "TRUNCATE TABLE cuenta_bancaria, moneda, pais, precio_moneda, usuario, usuario_tiene_moneda"
cursor.execute(query)
connection.commit()

print("Generando Datos...")
now = datetime.now()

paises = [
    (1, 'Angola'),
    (2, 'Sudáfrica'),
    (3, 'Canadá'),
    (4, 'Estados Unidos'),
    (5, 'Chile'),
    (6, 'Australia'),
    (7, 'India'),
    (8, 'Corea del Sur'),
    (9, 'Rusia'),
    (10, 'Suiza'),
]

monedas = [
    (1, 'BTC', 'Bitcoin'),
    (2, 'ETH', 'Ethereum'),
    (3, 'LTC', 'Litecoin'),
    (4, 'DOGE', 'Dogecoin'),
    (5, 'USDT', 'Tether USD'),
    (6, 'XLM', 'Stellar Lumens'),
    (7, 'XRP', 'Ripple'),
    (8, 'BCC', 'Bitconnect'),
    (9, 'DRCY', 'Prestigiocoin'),
    (10, 'RP', 'Riot Points')
]

#precio_moneda
precios_monedas = []
for idMoneda in range(1,11):
    n_cambios = r.randint(5,25)
    to_add = []
    for i in range(n_cambios):
        td = timedelta(
            weeks=r.randint(0,51),
            days=r.randint(0, 6),
            hours=r.randint(0, 23),
            minutes=r.randint(0, 59),
            seconds=r.randint(0, 59)
        )
        to_add.append((idMoneda, now - td, r.randint(1, 10000)/10))
    to_add.sort()
    precios_monedas = precios_monedas + to_add

def generateFecha():
    y = r.randint(2015,2019)
    m = r.randint(1,12)
    d = r.randint(1,31)
    if m in [4, 6, 9, 11] and d > 30:
        d = 30
    if m == 2 and d > 28:
        d = 28
    return datetime(y,m,d)
    
usuarios = [
    (0, 'Admin', 'Admin',       'admin@admin',                 '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly',           r.randint(1,10), generateFecha(), True),
    (1, 'Carlos', 'Matos',      'carlos.matos@bitconnect.com', '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (2, 'Kaidan', 'Jones',      'kaidan.jones@gmail.com',      '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (3, 'Dimitri', 'Knights',   'dimitri.knights@yahoo.com',   '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (4, 'Seb', 'Cope',          'seb.cope@hotmail.com',        '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (5, 'Bella', 'Hamilton',    'bella.hamilton@outlook.com',  '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (6, 'Khadijah', 'Briggs',   'khadijah.briggs@msn.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (7, 'Marcelo', 'Panire',    'marcelo.panire@gmail.com',    '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (8, 'Shola', 'Shea',        'shola.shea@msn.com',          '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (9, 'Dayna', 'Mcclain',     'dayna.mcclain@gmail.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (10, 'Henri', 'Wicks',      'henri.wicks@hotmail.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (11, 'Willow', 'Fuller',    'willow.fuller@yahoo.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (12, 'Odin', 'Lopez',       'odin.lopez@hotmail.com',      '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (13, 'Aqeel', 'Blundell',   'aqeel.blundell@outlook.com',  '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (14, 'Cecilia', 'Reyes',    'cecilia.reyes@gmail.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (15, 'Evelyn', 'Pratt',     'evelyn.pratt@msn.com',        '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (16, 'Gloria', 'Connelly',  'gloria.connelly@yahoo.com',   '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (17, 'Samanta', 'Carter',   'samanta.carter@hotmail.com',  '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (18, 'Gracie-May', 'Beech', 'graciemay.beech@outlook.com', '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (19, 'Ferne', 'Norman',     'ferne.norman@gmail.com',      '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (20, 'Kimberly', 'Richard', 'kimberly.richard@gmail.com',  '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (21, 'Anwar', 'Bains',      'anwar.bains@outlook.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (22, 'Reon', 'Mcneil',      'reon.mcneil@gmail.com',       '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (23, 'Saqib', 'Andrews',    'saqib.andrews@yahoo.com',     '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (24, 'Elif', 'Floyd',       'elif.floyd@hotmail.com',      '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False),
    (25, 'Mai', 'Duffy',        'mai.duffy@yahoo.com',         '$2y$12$0AhiZRjZ/fGQFtBYAPfIuuOVHVTb83PhtvTjznO9XuSPdhSbNMAly', r.randint(1,10), generateFecha(), False)
]

#cuenta_bancaria + usuario_tiene_moneda
cuentas_bancarias = [(1, 1, 0.01)]
usuario_tiene_moneda = [(1, 8, round(r.uniform(70.0, 100.0), 2))]
options = [i for i in range(1, 11)]
N_CTA = 2
for i in range(2, 26):
    n_ctas = r.randint(0,3)
    to_add = []
    for j in range(n_ctas):
        to_add.append((N_CTA, i, round(r.uniform(0.0, 10000.0), 2)))
        N_CTA = N_CTA + 1
    cuentas_bancarias = cuentas_bancarias + to_add
    n_monedas = r.randint(0,3)
    m = r.sample(options, k=n_monedas)
    for j in m:
        usuario_tiene_moneda.append((i, j, round(r.uniform(0.0, 100.0), 2)))

print("Insertando Datos...")

insert = [
    "INSERT INTO pais (cod_pais, nombre) VALUES (%s, %s)",
    "INSERT INTO moneda (id, sigla, nombre) VALUES (%s, %s, %s)",
    "INSERT INTO precio_moneda (id_moneda, fecha, valor) VALUES (%s, %s, %s)",
    "INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, administrador) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO cuenta_bancaria (numero_cuenta, id_usuario, balance) VALUES (%s, %s, %s)",
    "INSERT INTO usuario_tiene_moneda (id_usuario, id_moneda, balance) VALUES (%s, %s, %s)"
]
for pais in paises:
    cursor.execute(insert[0], pais)
for moneda in monedas:
    cursor.execute(insert[1], moneda)
for precio_moneda in precios_monedas:
    cursor.execute(insert[2], precio_moneda)
for usuario in usuarios:
    cursor.execute(insert[3], usuario)
for cuenta_bancaria in cuentas_bancarias:
    cursor.execute(insert[4], cuenta_bancaria)
for utm in usuario_tiene_moneda:
    cursor.execute(insert[5], utm)
connection.commit()
print("Todo Listo!")