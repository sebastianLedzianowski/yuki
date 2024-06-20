import jwt
from django.conf import settings
from django.utils import timezone


def generate_jwt_token(item_id, days_valid, minutes_valid):
    expiration = timezone.now() + timezone.timedelta(days=days_valid, minutes=minutes_valid)
    token = jwt.encode({
        'item_id': item_id,
        'exp': expiration
    }, settings.SECRET_KEY, algorithm='HS256')
    return token


def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        workshop_id = payload['item_id']
        expiration = payload['exp']
        if expiration < timezone.now().timestamp():
            return None
        return workshop_id
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None