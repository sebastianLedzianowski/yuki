import jwt
from django.conf import settings
from datetime import datetime, timedelta, timezone


def generate_jwt_token(workshop_id):
    expiration = datetime.utcnow() + timedelta(days=30)
    token = jwt.encode({
        'workshop_id': workshop_id,
        'exp': expiration
    }, settings.SECRET_KEY, algorithm='HS256')
    return token


def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        workshop_id = payload['workshop_id']
        expiration = payload['exp']
        if expiration < timezone.now().timestamp():
            return None
        return workshop_id
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None