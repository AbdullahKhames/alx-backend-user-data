from flask import request, jsonify, abort
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    if email is None or email == '':
        return jsonify({ "error": "email missing" }), 400
    password  = request.form.get('password')
    if password  is None or password  == '':
        return jsonify({ "error": "password missing" }), 400
    users = User.search({'email': email})
    user = None
    for u in users:
        if u.email == email:
            user = u
    if user is None:
        return jsonify({ "error": "no user found for this email" }), 404
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    out = jsonify(user.to_json(True))
    out.set_cookie(getenv('SESSION_NAME'), session_id)
    return out


@app_views.route('/auth_session/logout/', methods=['DELETE'], strict_slashes=False)
def logout():
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    else:
        return jsonify({}), 200
