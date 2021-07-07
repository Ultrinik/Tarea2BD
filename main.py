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

#PAIS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def crear_pais():
	json = request.get_json(force=True)

	if json.get('cod_pais') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	pais = Pais.create(json['cod_pais'],json['nombre'])

	return jsonify({'usuario': pais.json() })
	
if __name__ == '__main__':
	app.run(debug=True)
