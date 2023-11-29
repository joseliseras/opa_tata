from flask_sqlalchemy import SQLAlchemy

#instanciamos la base de datos

db = SQLAlchemy()

#Creamos nuestro modelo de base de datos

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    telefono = db.Column(db.String(250))
    email= db.Column(db.String(250))
    ciudad = db.Column(db.String(250))
    cantidad_agua = db.Column(db.String(250))
    incidente = db.Column(db.String(250))                

