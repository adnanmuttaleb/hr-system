from functools import wraps
from flask import current_app, request, abort

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def is_admin(view):
    @wraps(view)
    def wrap(*args, **kwargs):
        admin = request.headers.get('X-ADMIN')
        if not admin or int(admin) != 1:
            abort(403)
        return view(*args, **kwargs)
    return wrap
