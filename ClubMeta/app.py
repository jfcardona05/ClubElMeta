from flask import Flask
from flask_jwt_extended import JWTManager
from routes.index_routes import index_bp
from routes.actividades_routes import actividades_bp
from routes.eventos_routes import eventos_bp
from routes.nosotros_routes import nosotros_bp
from routes.membresias_routes import membresias_bp
from routes.sesion_routes import sesion_bp
from routes.registrar_routes import registrar_bp
from routes.administrador_routes import administrador_bp
from routes.empleado_routes import empleado_bp
from routes.usuario_routes import usuario_bp


app = Flask(__name__, template_folder="templates", static_folder="static")

app.config["JWT_SECRET_KEY"] = "clave-super-secreta"
jwt = JWTManager(app)

# Registrar blueprints (rutas a los modulos)
app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(actividades_bp, url_prefix="/")
app.register_blueprint(eventos_bp, url_prefix="/")
app.register_blueprint(nosotros_bp, url_prefix="/")
app.register_blueprint(membresias_bp, url_prefix="/")
app.register_blueprint(sesion_bp, url_prefix="/")
app.register_blueprint(registrar_bp, url_prefix="/")
app.register_blueprint(administrador_bp, url_prefix="/")
app.register_blueprint(empleado_bp, url_prefix="/")
app.register_blueprint(usuario_bp, url_prefix="/")





if __name__ == '__main__':
    app.run(debug=True)
