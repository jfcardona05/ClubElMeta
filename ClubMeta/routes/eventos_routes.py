from flask import Blueprint, render_template

eventos_bp = Blueprint("eventos", __name__)

@eventos_bp.route('/eventos')
def eventos():
    return render_template("eventos.html")
