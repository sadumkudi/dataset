import jwt

# The JWT you want to decode
encoded_jwt = 'your.jwt.token.here'

# If you know the secret key and the JWT uses a symmetric algorithm like HMAC (HS256, HS384, HS512)
secret_key = 'your-secret-key'

# Decoding without validation (not recommended for production)
decoded_jwt = jwt.decode(encoded_jwt, options={"verify_signature": False})
print(decoded_jwt)

# Decoding with signature validation
try:
    decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
    print(decoded_jwt)
except jwt.InvalidTokenError as e:
    print(f"Token validation error: {e}")
