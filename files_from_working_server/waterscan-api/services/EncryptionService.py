from werkzeug import security

class EncryptionService:
    @staticmethod
    def hashPassword(password):
        """Returns a hashed password"""
        return security.generate_password_hash(password,method='pbkdf2:sha256', salt_length=8)

    @staticmethod
    def checkPassword(hash, password):
        """Returns a verified password"""
        return security.check_password_hash(hash, password)