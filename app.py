from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "aplicacion": "API de ejemplo para la tarea de Arquitectura Back-End",
        "version": "1.0",
        "descripcion": "Esta API demuestra el uso de endpoints con Flask."
    })


# Ruta POST /mensaje
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    mensaje_usuario = data.get("mensaje", "No enviaste mensaje")

    return jsonify({
        "respuesta": f"Recibí tu mensaje: {mensaje_usuario}"
    })


if __name__ == "__main__":
    app.run(debug=True)