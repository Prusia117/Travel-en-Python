from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from modules.dijkstra import dijkstra

app = Flask(__name__)
CORS(app) 

@app.route('/dijkstra', methods=['POST'])
def dijkstra_route():
    data = request.get_json()
    
    if not data or 'first_country' not in data or 'second_country' not in data:
        return jsonify({"error": "Faltan parámetros"}), 400
    
    first_country = data['first_country']
    second_country = data['second_country']

    dijkstra_instance = dijkstra(first_country, second_country)
    
    if dijkstra_instance in ['El país de origen y el país de destino son iguales.', 'Uno de los países no está en la lista.']:
        return jsonify({"error": dijkstra_instance}), 400

    distance, secuence = dijkstra_instance

    return jsonify({
        "distance": distance,
        "secuence": secuence
    })

if __name__ == '__main__':
    app.run(debug=True)
