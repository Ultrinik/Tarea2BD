from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
	__tablename__ = 'usuario'
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False) 
	apellido = db.Column(db.String(50), nullable=True) 
	correo = db.Column(db.String(50), nullable=False) 
	contraseña = db.Column(db.String(50), nullable=False) 
	fecha_registro = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
	
	@classmethod
	def create(cls, nm, ap, mail, pass):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		usuario = Usuario(nombre=nm,apellido=ap,correo=mail,contraseña=pass)
		return usuario.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido': self.apellido,
			'correo': self.correo,
			'contraseña': self.contraseña,
			'fecha_registro': self.fecha_registro
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Pais(db.Model):
	__tablename__ = 'pais'
	cod_pais = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(45), nullable=False)
	
	@classmethod
	def create(cls, nm):
		pais = Pais(nombre=nm)
		return pais.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'cod_pais': self.cod_pais,
			'nombre': self.nombre
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Cuenta_bancaria(db.Model):
	__tablename__ = 'cuenta_bancaria'
	numero_cuenta = db.Column(db.Integer, primary_key=True)
	id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
	balance = db.Column(db.Float, nullable=False)
	
	@classmethod
	def create(cls, bl):
		balance = Cuenta_bancaria(balance=bl)
		return balance.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Usuario_tiene_moneda(db.Model):
	__tablename__ = 'usuario_tiene_moneda'
	id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key=True)
	id_moneda = db.Column(db.Integer, db.ForeignKey("moneda.id"), primary_key=True)
	balance = db.Column(db.Float, nullable=False)
	
	@classmethod
	def create(cls, bl):
		balance = Usuario_tiene_moneda(balance=bl)
		return balance.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Moneda(db.Model):
	__tablename__ = 'moneda'
	id = db.Column(db.Integer, primary_key=True)
	sigla = db.Column(db.String(10), nullable=False)
	nombre = db.Column(db.String(80), nullable=False)
	
	@classmethod
	def create(cls, sg, nm):
		moneda = Moneda(sigla=sg, nombre=nm)
		return moneda.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'sigla': self.sigla,
			'nombre': self.nombre
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False

class Precio_moneda(db.Model):
	__tablename__ = 'moneda'
	id_moneda = db.Column(db.Integer, db.ForeingKey("moneda.id"), primary_key=True)
	fecha = db.Column(db.DateTime(), nullable=False, primary_key=True)
	valor = db.Column(db.Float, nullable=False)
	
	@classmethod
	def create(cls, dt, vl):
		precio_moneda = Precio_moneda(fecha=dt, valor=vl)
		return precio_moneda.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'fecha': self.fecha,
			'valor': self.valor
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except:
			return False