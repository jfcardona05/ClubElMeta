from flask import Blueprint, render_template

actividades_bp = Blueprint("actividades", __name__)

@actividades_bp.route('/actividades')
def actividades():
    return render_template("actividades.html")
