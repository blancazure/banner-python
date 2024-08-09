from flask import Flask, request, jsonify
import pyfiglet
import argparse

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
    parser = argparse.ArgumentParser(description='Servidor que genera banners ASCII.')
    parser.add_argument('-p', '--port', type=int, default=5000, help='Puerto en el que se ejecutará el servidor.')
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port)
