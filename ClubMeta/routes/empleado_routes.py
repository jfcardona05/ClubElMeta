from flask import Blueprint, render_template

empleado_bp = Blueprint("empleado", __name__)

@empleado_bp.route('/empleado')
def empleado():
    return render_template("empleado.html")
