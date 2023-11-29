from flask import Flask, request, jsonify, render_template, url_for
import folium
from modelos import db,Marker

#from modelos import db,Marker
app = Flask(__name__)

#CONFIGURACION DEL TIPO DE BASE DE DATOS
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#iNICIALIZACION DE LA BASE DE DATOS 
db.init_app(app)



##RUTAS

#PAGINA PRINCIPAL PARA VISUALIZACION DE MAPAS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acceso_ciudadano2')
def acceso_ciudadano():
    return render_template('acceso_ciudadano2.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

#PAGINA PARA GUARDAR MARCADORES A LA DB
@app.route('/save_marker', methods=['POST'])
def save_marker():
    data = request.json
    new_marker = Marker(latitude=data['lat'], longitude=data['lng'], nombre=data['nombre'],apellido=data['apellido'],telefono = data['telefono'], email=data['email'],ciudad=data['ciudad'],cantidad_agua=data['cantidad_agua'], incidente=data['incidente'])
    db.session.add(new_marker)
    db.session.commit()
    return jsonify({'status': 'success', 'id': new_marker.id})

#PAGINA PARA LEER MARCADORES DE LA DB
@app.route('/get_markers', methods=['GET'])
def get_markers():
    markers = Marker.query.all()
    markers_data = [{"latitude": marker.latitude,  "longitude": marker.longitude, "id": marker.id, "nombre":marker.nombre, "apellido":marker.apellido, "telefono":marker.telefono, "email":marker.email, "ciudad":marker.ciudad,"cantidad_agua":marker.cantidad_agua, "incidente":marker.incidente} for marker in markers]
    return jsonify(markers_data)

@app.route('/update_marker/<int:id>', methods=['POST'])
def update_marker(id):
    data = request.get_json()
    marker = Marker.query.get(id)
    if marker:
        marker.nombre = data['nombre']
        marker.apellido = data['apellido']
        marker.telefono = data['telefono']
        marker.email = data['email']
        marker.ciudad = data['ciudad']
        marker.cantidad_agua = data['cantidad_agua']
        marker.incidente = data['incidente']
        marker.latitude = data['latitude']
        marker.longitude = data['longitude']
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'marker not found'}), 404
    
@app.route('/delete_marker/<int:id>', methods=['DELETE'])
def delete_marker(id):
    marker = Marker.query.get(id)
    if marker:
        db.session.delete(marker)
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'marker not found'}), 404




if __name__ == '__main__':
    app.run(debug=True)