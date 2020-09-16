import jwt

def set_tocken(payload, expiry, secret):

    __payload = {'exp' : expiry}
    __payload.update(payload)
    return jwt.encode(__payload, secret, algorithm='HS256')

def get_tocken(tocken,secret):
    try:
        return jwt.decode(tocken, secret, algorithm='HS256')
    except Exception:
        return None


