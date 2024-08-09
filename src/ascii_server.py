from flask import Flask, request, jsonify
import pyfiglet
import os

app = Flask(__name__)

@app.route('/generarbaner', methods=['GET'])
def generar_baner():
    texto = request.args.get('texto')
    if not texto:
        return jsonify({'error': 'El parámetro "texto" es requerido.'}), 400
    
    # Generar el banner en ASCII
    ascii_banner = pyfiglet.figlet_format(texto)
    
    # Retornar el banner
    return f"{ascii_banner}"

if __name__ == "__main__":
    # Obtener el puerto de la variable de entorno PUERTO_SERVIDOR o usar 5000 por defecto
    port = int(os.getenv("PUERTO_SERVIDOR", 5000))
    app.run(host='0.0.0.0', port=port)