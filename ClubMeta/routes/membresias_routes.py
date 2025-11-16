from flask import Blueprint, render_template

membresias_bp = Blueprint("membresias", __name__)

@membresias_bp.route('/membresias')
def membresias():
    return render_template("membresias.html")
