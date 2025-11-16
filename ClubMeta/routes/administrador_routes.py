from flask import Blueprint, render_template

administrador_bp = Blueprint("administrador", __name__)

@administrador_bp.route('/administrador')
def administrador():
    return render_template("administrador.html")
