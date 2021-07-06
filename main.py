from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import User
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

# Endpoint para obtener todos los usuarios
@app.route('/api/v1/users', methods=['GET'])
def get_users():
	users = [ user.json() for user in User.query.all() ] 
	return jsonify({'users': users })

# Endpoint para obtener el usuario con id <id>
@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
	user = User.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'User does not exists'}), 404

	return jsonify({'user': user.json() })

# Endpoint para insertar un usuario en la bd
@app.route('/api/v1/users/', methods=['POST'])
def create_user():
	json = request.get_json(force=True)

	if json.get('username') is None:
		return jsonify({'message': 'El formato está mal'}), 400

	user = User.create(json['username'])

	return jsonify({'user': user.json() })

# Endpoint para actualizar los datos de un usuario en la bd
@app.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
	user = User.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'User does not exists'}), 404

	json = request.get_json(force=True)
	if json.get('username') is None:
		return jsonify({'message': 'Bad request'}), 400

	user.username = json['username']

	user.update()

	return jsonify({'user': user.json() })

# Endpoint para eliminar el usuario con id igual a <id>
@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.filter_by(id=id).first()
	if user is None:
		return jsonify({'message': 'El usuario no existe'}), 404

	user.delete()

	return jsonify({'user': user.json() })

if __name__ == '__main__':
	app.run(debug=True)
