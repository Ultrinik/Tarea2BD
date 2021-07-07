from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Usuario
from models import Pais
from models import Cuenta_bancaria
from models import Moneda
from models import Precio_moneda
from models import Usuario_tiene_moneda
from flask import request

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)

#USUARIO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/usuario/', methods=['POST'])
def crear_usuario():
	json = request.get_json(force=True)

	if json.get('id') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	usuario = Usuario.create(json['id'],json['nombre'],json['apellido'],json['correo'],json['contraseña'], json['pais'])

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

	usuario.nombre = json['nombre']
	usuario.apellido = json['apellido']
	usuario.correo = json['correo']
	usuario.contraseña = json['contraseña']
	usuario.pais = json['pais']
	usuario.update()
	return jsonify({'usuario': usuario.json() })

#PAIS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/pais/', methods=['POST'])
def crear_pais():
	json = request.get_json(force=True)

	if json.get('cod_pais') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	pais = Pais.create(json['cod_pais'],json['nombre'])

	return jsonify({'pais': pais.json() })

@app.route('/api/pais/<cod_pais>', methods=['DELETE'])
def delete_pais(cod_pais):
	pais = Pais.query.filter_by(cod_pais=cod_pais).first()
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

	pais.nombre = json['nombre']
	pais.update()
	return jsonify({'pais': pais.json() })

#CUENTA BANCARIA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/cuenta_bancaria/', methods=['POST'])
def crear_cuenta_bancaria():
	json = request.get_json(force=True)

	if json.get('numero_cuenta') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	numero_cuenta = Cuenta_bancaria.create(json['numero_cuenta'],json['id_usuario'],json['balance'])

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

	cuenta_bancaria.id_usuario = json['id_usuario']
	cuenta_bancaria.balance = json['balance']
	cuenta_bancaria.update()
	return jsonify({'cuenta_bancaria': cuenta_bancaria.json() })

#USUARIO TIENE MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/usuario_tiene_moneda/', methods=['POST'])
def crear_usuario_tiene_moneda():
	json = request.get_json(force=True)

	if json.get('id_usuario') is None:
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
	usuario_tiene_moneda = Usuario_tiene_moneda.query.filter_by(id_moneda=id_moneda,id_usuario=id_usuario).first()
	if usuario_tiene_moneda is None:
		return jsonify({'message': 'El usuario indicado no tiene la moneda indicada'}), 404
	json = request.get_json(force=True)

	usuario_tiene_moneda.balance = json['balance']

	usuario_tiene_moneda.update()
	return jsonify({'usuario_tiene_moneda': usuario_tiene_moneda.json() })

#MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/moneda/', methods=['POST'])
def crear_moneda():
	json = request.get_json(force=True)

	if json.get('id') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	moneda = Moneda.create(json['id'],json['sigla'],json['nombre'])

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

	moneda.sigla = json['sigla']
	moneda.nombre = json['nombre']
	moneda.update()
	return jsonify({'moneda': moneda.json() })

#PRECIO MONEDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/api/precio_moneda/', methods=['POST'])
def crear_precio_moneda():
	json = request.get_json(force=True)

	if json.get('id_moneda') is None:
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

@app.route('/api/precio_moneda/<id_moneda>/<fecha>', methods=['PUT'])
def update_precio_moneda(id,fecha):
	precio_moneda = Precio_moneda.query.filter(Precio_moneda.id_moneda==id,Precio_moneda.fecha==fecha).first()
	if precio_moneda is None:
		return jsonify({'message': 'La moneda indicada no tiene valores para la fecha indicada'}), 404
	json = request.get_json(force=True)

	precio_moneda.valor = json['valor']
	precio_moneda.update()
	return jsonify({'precio_moneda': precio_moneda.json() })
	
if __name__ == '__main__':
	app.run(debug=True)
