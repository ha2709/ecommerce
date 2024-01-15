import secrets
import hashlib


def generate_verification_token():
    # Generate a random string as the token
    token = secrets.token_urlsafe(32)  # Generate a 256-bit random token

    # Hash the token (optional but recommended for security)
    token_hash = hashlib.sha256(token.encode()).hexdigest()

    return token_hash
