from cryptography.fernet import Fernet, InvalidToken

# Ek baar generate karke yaha paste kar lo
SECRET_KEY = b'WkJtV1dOdGd5Q2h6N0ltcTRsWUhScW1qN1RPTDg4c2I='  

fernet = Fernet(SECRET_KEY)

def get_password_hash(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()

def verify_password(plain_password: str, encrypted_password: str) -> bool:
    try:
        decrypted = fernet.decrypt(encrypted_password.encode()).decode()
        return decrypted == plain_password
    except InvalidToken:
        return False
