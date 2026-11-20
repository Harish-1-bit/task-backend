from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(planPassword : str, hasedPassword: str):
    return password_hash.verify(planPassword, hasedPassword)