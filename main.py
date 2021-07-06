from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import *
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

	if json.get('nombre') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	usario = Usuario.create(json['nombre'],json['apellido'],json['correo'],json['contraseña'],json['fecha_registro'])

	return jsonify({'usario': usario.json() })

if __name__ == '__main__':
	app.run(debug=True)
