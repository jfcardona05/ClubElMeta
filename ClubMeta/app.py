from flask import Flask, jsonify, request, send_file
import bcrypt, os
from flask_jwt_extended import JWTManager, create_access_token
from conexion import conexion

app = Flask(__name__, template_folder="templates", static_folder="", static_url_path="")

 

app.config["JWT_SECRET_KEY"] = "clave-super-secreta"  # cámbiala por una clave real
jwt = JWTManager(app)
@app.route('/sesion', methods=['GET'])
def login_page():
    return send_file(os.path.join(app.root_path, 'templates', 'sesion.html'))


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not correo or not contrasena:
        return jsonify({"message": "Correo y contraseña son obligatorios"}), 400

    conn = conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, nombre, correo, telefono, contrasena, rol_id AS rol 
        FROM usuarios 
        WHERE correo = %s
    """, (correo,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

       

    if contrasena != user['contrasena']:
        return jsonify({"message": "Usuario o contraseña incorrectos"}), 401


   
    token = create_access_token(identity=correo, additional_claims={"rol": user['rol']})

  
    if user['rol'] == 1:
        dashboard_url = "/dashboard/Administrador"
        role_name = "Administrador"
    elif user['rol'] == 2:
        dashboard_url = "/dashboard/Empleado"
        role_name = "Empleado"
    elif user['rol'] == 3:
        dashboard_url = "/dashboard/Usuario"
        role_name = "Usuario"
    else:
        dashboard_url = "/"
        role_name = "Desconocido"

    return jsonify({
        "message": "Autenticación exitosa",
        "access_token": token,
        "role": role_name,
        "dashboard_url": dashboard_url
    }), 200


@app.route('/', methods=['GET'])
def home():
    return send_file(os.path.join(app.root_path, "templates", "index.html"))


if __name__ == '__main__':
    app.run(debug=True)
