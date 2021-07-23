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
	pais = db.Column(db.Integer, db.ForeignKey("pais.cod_pais"))
	fecha_registro = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

	cuenta_bancaria = db.relationship('Cuenta_bancaria', cascade="all,delete", backref="parent_user", lazy='dynamic')
	usuario_tiene_moneda = db.relationship('Usuario_tiene_moneda', cascade="all,delete", backref="parent_user", lazy='dynamic')
	
	
	@classmethod
	def create(cls, id_, nm, ap, mail, pss, ct):
		# Instanciamos un nuevo usuario y lo guardamos en la bd
		usuario = Usuario(id=id_,nombre=nm,apellido=ap,correo=mail,contraseña=pss,pais=ct)
		return usuario.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except Exception as e:
			print(str(e))
			return False
	def json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido': self.apellido,
			'correo': self.correo,
			'contraseña': self.contraseña,
			'pais': self.pais,
			'fecha_registro': str(self.fecha_registro)
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except Exception as e:
			print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
			print(e)
			print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
			return False

class Pais(db.Model):
	__tablename__ = 'pais'
	cod_pais = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(45), nullable=False)
	
	usuario = db.relationship('Usuario', cascade="all,delete", backref="parent_pais", lazy='dynamic')
	
	@classmethod
	def create(cls,cp, nm):
		pais = Pais(cod_pais=cp, nombre=nm)
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
	def create(cls, nc, iu, bl):
		cuenta_bancaria = Cuenta_bancaria(numero_cuenta=nc, id_usuario=iu, balance=bl)
		return cuenta_bancaria.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'numero_cuenta': self.numero_cuenta,
			'id_usuario': self.id_usuario,
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
	def create(cls, iu, im, bl):
		usuario_tiene_moneda = Usuario_tiene_moneda(id_usuario=iu, id_moneda=im, balance=bl)
		return usuario_tiene_moneda.save()

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()

			return self
		except:
			return False
	def json(self):
		return {
			'id_usuario': self.id_usuario,
			'id_moneda': self.id_moneda,
			'balance': self.balance
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except Exception as e:
			print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
			print(e)
			print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
			return False

class Moneda(db.Model):
	__tablename__ = 'moneda'
	id = db.Column(db.Integer, primary_key=True)
	sigla = db.Column(db.String(10), nullable=False)
	nombre = db.Column(db.String(80), nullable=False)
	
	usuario_tiene_moneda = db.relationship('Usuario_tiene_moneda', cascade="all,delete", backref="parent_coin", lazy='dynamic')
	precio_moneda = db.relationship('Precio_moneda', cascade="all,delete", backref="parent_coin", lazy='dynamic')

	@classmethod
	def create(cls,id_, sg, nm):
		moneda = Moneda(id=id_, sigla=sg, nombre=nm)
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
			'id': self.id,
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
	__tablename__ = 'precio_moneda'
	id_moneda = db.Column(db.Integer, db.ForeignKey("moneda.id"), primary_key=True)
	fecha = db.Column(db.DateTime(), nullable=False, primary_key=True)
	valor = db.Column(db.Float, nullable=False)
	
	@classmethod
	def create(cls, im, dt, vl):
		precio_moneda = Precio_moneda(id_moneda=im, fecha=dt, valor=vl)
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
			'id_moneda': self.id_moneda,
			'fecha': str(self.fecha),
			'valor': self.valor
		}
	def update(self):
		self.save()
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()

			return True
		except Exception as e:
			print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
			print(e)
			print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
			return False