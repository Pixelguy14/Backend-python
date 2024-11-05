import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'HAGAN_BACKUPS'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({ 'message': 'Token no encontrado'}), 403
        
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token invalid'}), 403
        return f(*args, **kwargs)
    return decorated
