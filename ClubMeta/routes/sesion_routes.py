from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
import bcrypt
from conexion import conexion

sesion_bp = Blueprint("sesion", __name__)

@sesion_bp.route('/sesion')
def sesion():
    return render_template("sesion.html")


@sesion_bp.route('/login', methods=['POST'])
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

    # Validar contraseña
    if not bcrypt.checkpw(contrasena.encode('utf-8'), user['contrasena'].encode('utf-8')):
        return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

    # Crear token JWT
    token = create_access_token(identity=correo, additional_claims={"rol": user['rol']})

    # Redirección según rol
    if user['rol'] == 1:
        dashboard_url = "administrador"
        role_name = "Administrador"
    elif user['rol'] == 2:
        dashboard_url = "empleado"
        role_name = "Empleado"
    elif user['rol'] == 3:
        dashboard_url = "usuario"
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

