from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Datos que el bot leerá (esto es lo que cambiarás cuando quieras buscar otra cosa)
ORDEN_MAESTRA = {
    "buscar": "Honda Civic rojo",
    "token": "7IrKGL6WJqVEiNa8Q0fos", 
    "status": "activo"
}

@app.route('/api', methods=['GET'])
def obtener_orden():
    token_cliente = request.args.get('token')
    if token_cliente == ORDEN_MAESTRA['token']:
        return jsonify(ORDEN_MAESTRA)
    return jsonify({"error": "No autorizado"}), 403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)