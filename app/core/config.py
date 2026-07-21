import os


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "careergraph-dev-secret-key-change-before-production",
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24