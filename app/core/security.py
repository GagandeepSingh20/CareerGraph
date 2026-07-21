from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(plain_password: str) -> str:
    """Convert a plain password into a secure hashed password."""
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against the stored hashed password."""
    return password_hash.verify(plain_password, hashed_password)