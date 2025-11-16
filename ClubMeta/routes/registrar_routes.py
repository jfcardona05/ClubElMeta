from flask import Blueprint, render_template
from flask import Blueprint, request, jsonify, render_template
import bcrypt
from conexion import conexion

registrar_bp = Blueprint("registrar", __name__)

@registrar_bp.route('/registrar')
def registrar():
    return render_template("registrar.html")

@registrar_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()

    nombre = data.get('nombre')
    correo = data.get('correo')
    telefono = data.get('telefono')
    contrasena = data.get('contrasena')
    rol_id = 3

    if not nombre or not correo or not telefono or not contrasena:
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    conn = conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({"message": "El correo ya está registrado"}), 409

    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    cursor.execute("""
        INSERT INTO usuarios (nombre, correo, telefono, contrasena, rol_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (nombre, correo, telefono, contrasena_hash, rol_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201

