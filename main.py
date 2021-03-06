from flask import Flask
from flask import jsonify, json
from config import config
from models import db
from models import Usuario
from models import Pais
from models import Cuenta_bancaria
from models import Moneda
from models import Precio_moneda
from models import Usuario_tiene_moneda
from flask import request
from sqlalchemy.sql.expression import func
import decimal


class MyJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	app.json_encoder = MyJSONEncoder
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)

#USUARIO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/usuario/', methods=['GET'])
def get_usuarios():
	data = Usuario.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/usuario/<id>', methods=['GET'])
def get_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'usuario does not exists'}), 404

	return jsonify({'usuario': usuario.json() })

@app.route('/api/usuario/', methods=['POST'])
def crear_usuario():
	json = request.get_json(force=True)
	
	max_id = db.session.execute(db.session.query(func.max(Usuario.id))).first()[0] + 1

	usuario = Usuario.create(id_=max_id,nm=json['nombre'],ap=json['apellido'],mail=json['correo'],pss=json['contraseña'], ct=json['pais'])

	return jsonify({'usuario': usuario.json() })

@app.route('/api/usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	usuario.delete()

	return jsonify({'usuario': usuario.json() })

@app.route('/api/usuario/<id>', methods=['PUT'])
def update_user(id):
	usuario = Usuario.query.filter_by(id=id).first()
	if usuario is None:
		return jsonify({'message': 'El usuario no existe'}), 404
	json = request.get_json(force=True)

	if(json.get('id') != None): usuario.id = json['id']
	if(json.get('nombre') != None): usuario.nombre = json['nombre']
	if(json.get('apellido') != None): usuario.apellido = json['apellido']
	if(json.get('correo') != None): usuario.correo = json['correo']
	if(json.get('contraseña') != None): usuario.contraseña = json['contraseña']
	if(json.get('pais') != None): usuario.pais = json['pais']
	if(json.get('fecha_registro') != None): usuario.fecha_registro = json['fecha_registro']
	usuario.update()
	return jsonify({'usuario': usuario.json() })

#PAIS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/pais/', methods=['GET'])
def get_paises():
	data = Pais.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/pais/<cod_pais>', methods=['GET'])
def get_pais(cod_pais):
	print('GET '+str(cod_pais))
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
	if pais is None:
		return jsonify({'message': 'pais does not exists'}), 404

	return jsonify({'pais': pais.json() })

@app.route('/api/pais/', methods=['POST'])
def crear_pais():
	json = request.get_json(force=True)

	max_id = db.session.execute(db.session.query(func.max(Pais.cod_pais))).first()[0] + 1

	pais = Pais.create(max_id,json['nombre'])

	return jsonify({'pais': pais.json() })

@app.route('/api/pais/<pais_id>', methods=["DELETE"])
def delete_pais(pais_id):
	pais = Pais.query.filter_by(cod_pais=pais_id).first()
	if pais is None:
		return jsonify({'message': 'El pais no existe'}), 404

	pais.delete()

	return jsonify({'pais': pais.json() })

@app.route('/api/pais/<id>', methods=['PUT'])
def update_pais(id):
	pais = Pais.query.filter_by(cod_pais=id).first()
	if pais is None:
		return jsonify({'message': 'El pais no existe'}), 404
	json = request.get_json(force=True)
	if(json.get('cod_pais') != None): pais.cod_pais = json['cod_pais']
	if(json.get('nombre') != None): pais.nombre = json['nombre']
	pais.update()
	return jsonify({'pais': pais.json() })

#CUENTA BANCARIA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/cuenta_bancaria/', methods=['GET'])
def get_cuentas_bancarias():
	data = Cuenta_bancaria.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/cuenta_bancaria/<numero_cuenta>', methods=['GET'])
def get_cuenta_bancaria(numero_cuenta):
	cuenta_bancaria = Cuenta_bancaria.query.filter_by(numero_cuenta=numero_cuenta).first()
	if cuenta_bancaria is None:
		return jsonify({'message': 'cuenta_bancaria does not exists'}), 404

	return jsonify({'cuenta_bancaria': cuenta_bancaria.json() })

@app.route('/api/cuenta_bancaria/', methods=['POST'])
def crear_cuenta_bancaria():
	json = request.get_json(force=True)

	max_id = db.session.execute(db.session.query(func.max(Cuenta_bancaria.numero_cuenta))).first()[0] + 1

	numero_cuenta = Cuenta_bancaria.create(max_id,json['id_usuario'],json['balance'])

	return jsonify({'numero_cuenta': numero_cuenta.json() })

@app.route('/api/cuenta_bancaria/<numero_cuenta>', methods=['DELETE'])
def delete_cuenta_bancaria(numero_cuenta):
	cuenta_bancaria = Cuenta_bancaria.query.filter_by(numero_cuenta=numero_cuenta).first()
	if cuenta_bancaria is None:
		return jsonify({'message': 'La cuenta bancaria no existe'}), 404

	cuenta_bancaria.delete()

	return jsonify({'cuenta_bancaria': cuenta_bancaria.json() })

@app.route('/api/cuenta_bancaria/<id>', methods=['PUT'])
def update_cuenta_bancaria(id):
	cuenta_bancaria = Cuenta_bancaria.query.filter_by(numero_cuenta=id).first()
	if cuenta_bancaria is None:
		return jsonify({'message': 'Esta cuenta_bancaria no existe'}), 404
	json = request.get_json(force=True)

	if(json.get('numero_cuenta') != None): cuenta_bancaria.numero_cuenta = json['numero_cuenta']
	if(json.get('id_usuario') != None): cuenta_bancaria.id_usuario = json['id_usuario']
	if(json.get('balance') != None): cuenta_bancaria.balance = json['balance']
	cuenta_bancaria.update()
	return jsonify({'cuenta_bancaria': cuenta_bancaria.json() })

#USUARIO TIENE MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/usuario_tiene_moneda/', methods=['GET'])
def get_usuarios_tienen_monedas():
	data = Usuario_tiene_moneda.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/usuario_tiene_moneda/<id_usuario>/<id_moneda>', methods=['GET'])
def get_usuario_tiene_moneda(id_usuario,id_moneda):
	usuario_tiene_moneda = Usuario_tiene_moneda.query.filter(Usuario_tiene_moneda.id_usuario==id_usuario, Usuario_tiene_moneda.id_moneda==id_moneda).first()
	if usuario_tiene_moneda is None:
		return jsonify({'message': 'usuario_tiene_moneda does not exists'}), 404

	return jsonify({'usuario_tiene_moneda': usuario_tiene_moneda.json() })

@app.route('/api/usuario_tiene_moneda/', methods=['POST'])
def crear_usuario_tiene_moneda():
	json = request.get_json(force=True)

	if json.get('id_usuario') is None or json.get('id_moneda') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	usuario_tiene_moneda = Usuario_tiene_moneda.create(json['id_usuario'],json['id_moneda'],json['balance'])

	return jsonify({'usuario_tiene_moneda': usuario_tiene_moneda.json() })

@app.route('/api/usuario_tiene_moneda/<id_usuario>/<id_moneda>', methods=['DELETE'])
def delete_usuario_tiene_moneda(id_usuario,id_moneda):
	usuario_tiene_moneda = Usuario_tiene_moneda.query.filter(Usuario_tiene_moneda.id_usuario==id_usuario, Usuario_tiene_moneda.id_moneda==id_moneda).first()
	if usuario_tiene_moneda is None:
		return jsonify({'message': 'El usuario no tiene esta moneda'}), 404

	usuario_tiene_moneda.delete()

	return jsonify({'usuario_tiene_moneda': usuario_tiene_moneda.json() })

@app.route('/api/usuario_tiene_moneda/<id_moneda>/<id_usuario>', methods=['PUT'])
def update_usuario_tiene_moneda(id_moneda,id_usuario):
	usuario_tiene_moneda = Usuario_tiene_moneda.query.filter(Usuario_tiene_moneda.id_usuario==id_usuario, Usuario_tiene_moneda.id_moneda==id_moneda).first()
	if usuario_tiene_moneda is None:
		return jsonify({'message': 'El usuario indicado no tiene la moneda indicada'}), 404
	json = request.get_json(force=True)

	if(json.get('id_usuario') != None): usuario_tiene_moneda.id_usuario = json['id_usuario']
	if(json.get('id_moneda') != None): usuario_tiene_moneda.id_moneda = json['id_moneda']
	if(json.get('balance') != None): usuario_tiene_moneda.balance = json['balance']
	usuario_tiene_moneda.update()

	return jsonify({'usuario_tiene_moneda': usuario_tiene_moneda.json() })

#MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/moneda/', methods=['GET'])
def get_monedas():
	data = Moneda.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/moneda/<id>', methods=['GET'])
def get_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'moneda does not exists'}), 404

	return jsonify({'moneda': moneda.json() })

@app.route('/api/moneda/', methods=['POST'])
def crear_moneda():
	json = request.get_json(force=True)

	max_id = db.session.execute(db.session.query(func.max(Moneda.id))).first()[0] + 1

	moneda = Moneda.create(max_id,json['sigla'],json['nombre'])

	return jsonify({'moneda': moneda.json() })

@app.route('/api/moneda/<id>', methods=['DELETE'])
def delete_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'La moneda no existe'}), 404

	moneda.delete()

	return jsonify({'moneda': moneda.json() })

@app.route('/api/moneda/<id>', methods=['PUT'])
def update_moneda(id):
	moneda = Moneda.query.filter_by(id=id).first()
	if moneda is None:
		return jsonify({'message': 'La moneda no existe'}), 404
	json = request.get_json(force=True)

	if(json.get('id') != None): moneda.id = json['id']
	if(json.get('sigla') != None): moneda.sigla = json['sigla']
	if(json.get('nombre') != None): moneda.nombre = json['nombre']

	moneda.update()
	return jsonify({'moneda': moneda.json() })

#PRECIO MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/precio_moneda/', methods=['GET'])
def get_precio_monedas():
	data = Precio_moneda.query.all()
	return jsonify([i.json() for i in data])

@app.route('/api/precio_moneda/<id_moneda>/<fecha>', methods=['GET'])
def get_precio_moneda(id_moneda,fecha):
	print(id_moneda)
	print(fecha)
	fecha = fecha.replace('_', ' ')
	print(fecha)
	precio_moneda = Precio_moneda.query.filter(Precio_moneda.id_moneda==id_moneda, Precio_moneda.fecha==fecha).first()
	if precio_moneda is None:
		return jsonify({'message': 'precio_moneda does not exists'}), 404

	return jsonify({'precio_moneda': precio_moneda.json() })

@app.route('/api/precio_moneda/', methods=['POST'])
def crear_precio_moneda():
	json = request.get_json(force=True)

	if json.get('id_moneda') is None or json.get('fecha') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	precio_moneda = Precio_moneda.create(json['id_moneda'],json['fecha'],json['valor'])

	return jsonify({'id_moneda': precio_moneda.json() })
	
@app.route('/api/precio_moneda/<id_moneda>/<fecha>', methods=['DELETE'])
def delete_precio_moneda(id_moneda,fecha):
	precio_moneda = Precio_moneda.query.filter(Precio_moneda.id_moneda==id_moneda, Precio_moneda.fecha==fecha).first()
	if precio_moneda is None:
		return jsonify({'message': 'La moneda no ha tenido ese precio en esa fecha'}), 404

	precio_moneda.delete()

	return jsonify({'precio_moneda': precio_moneda.json() })

@app.route('/api/precio_moneda/<id>/<fecha>', methods=['PUT'])
def update_precio_moneda(id,fecha):
	precio_moneda = Precio_moneda.query.filter(Precio_moneda.id_moneda==id,Precio_moneda.fecha==fecha).first()
	if precio_moneda is None:
		return jsonify({'message': 'La moneda indicada no tiene valores para la fecha indicada'}), 404
	json = request.get_json(force=True)

	if(json.get('id_moneda') != None): precio_moneda.id_moneda = json['id_moneda']
	if(json.get('fecha') != None): precio_moneda.fecha = json['fecha']
	if(json.get('valor') != None): precio_moneda.valor = json['valor']

	precio_moneda.update()
	return jsonify({'precio_moneda': precio_moneda.json() })

@app.route('/api/consultas/<id>', methods=['POST'])
def get_consulta(id):
	print('Entrando a la consulta '+id)
	json = request.get_json(force=True)

	if(id == '1'):
		y = json['year']
		first = y+'-01-01'
		last = y+'-12-31'
		result = db.session.execute('SELECT * FROM usuario WHERE usuario.fecha_registro >= :first AND usuario.fecha_registro <= :last', {'first': first, 'last':last})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '2'):
		min = json['min']
		result = db.session.execute('SELECT numero_cuenta, balance FROM cuenta_bancaria WHERE cuenta_bancaria.balance > :min',{'min':min})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '3'):
		pais = json['pais']
		result = db.session.execute('SELECT pais.nombre as pais, usuario.nombre, usuario.apellido FROM usuario INNER JOIN pais ON usuario.pais = pais.cod_pais WHERE pais.nombre = :pais',{'pais':pais})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '4'):
		coin = json['coin']
		result = db.session.execute('SELECT nombre, MAX(valor) AS Max_valor FROM (SELECT moneda.nombre, precio_moneda.valor FROM moneda RIGHT JOIN precio_moneda ON precio_moneda.id_moneda = moneda.id WHERE moneda.nombre = :coin) AS tabla GROUP BY nombre',{'coin':coin})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '5'):
		sigla = json['sigla']
		result = db.session.execute('SELECT sigla as Moneda, SUM(balance) as Total FROM (SELECT moneda.sigla, usuario_tiene_moneda.balance FROM usuario_tiene_moneda LEFT JOIN moneda ON usuario_tiene_moneda.id_moneda = moneda.id WHERE sigla = :sigla) AS tabla GROUP BY sigla',{'sigla':sigla})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '6'):
		result = db.session.execute('SELECT moneda.sigla,COUNT(usuario_tiene_moneda.id_usuario) FROM usuario_tiene_moneda LEFT JOIN moneda ON usuario_tiene_moneda.id_moneda = moneda.id GROUP BY moneda.sigla ORDER BY count DESC LIMIT 3')
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '7'):
		mes = json['mes']
		print(mes)

		result = db.session.execute("SELECT nombre, MAX(cambios) AS max_cambios FROM (SELECT nombre, COUNT(to_char(fecha, 'YYYY-MM')) AS cambios, (SELECT to_char(fecha, 'YYYY-MM')) as mes FROM (SELECT moneda.nombre, precio_moneda.fecha FROM moneda RIGHT JOIN precio_moneda ON precio_moneda.id_moneda = moneda.id ) as tabla GROUP BY nombre, mes ) as tabla2 WHERE mes = :mes GROUP BY nombre ORDER BY max_cambios desc LIMIT 1",{'mes':mes})
		return jsonify({'result': [dict(row) for row in result]})
	elif(id == '8'):
		nombre = json['nombre']
		apellido = json['apellido']
		print(nombre, apellido)
		result = db.session.execute("SELECT top.nombre, top.apellido, moneda.nombre, top.balance FROM (SELECT nombre, apellido, usuario_tiene_moneda.id_moneda, usuario_tiene_moneda.balance FROM usuario LEFT JOIN usuario_tiene_moneda ON usuario.id = usuario_tiene_moneda.id_usuario WHERE  usuario.nombre = :nombre AND usuario.apellido = :apellido GROUP BY nombre, apellido, usuario_tiene_moneda.id_moneda, usuario_tiene_moneda.balance ORDER BY usuario_tiene_moneda.balance desc LIMIT 1) AS top JOIN moneda ON moneda.id = id_moneda",{'nombre':nombre, 'apellido':apellido})
		return jsonify({'result': [dict(row) for row in result]})

	else:
		jsonify({'message': 'Request inválido'}), 404


if __name__ == '__main__':
	app.run(debug=True)