from flask import render_template
from app.errors import bp

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500