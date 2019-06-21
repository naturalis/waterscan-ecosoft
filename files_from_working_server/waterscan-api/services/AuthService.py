from flask import request, jsonify, make_response
from services.TokenService import TokenService
from services.EncryptionService import EncryptionService
from functools import wraps
from models.User import User
from jwt.exceptions import InvalidTokenError

class AuthService:
    def tokenRequired(fn):
        """ Wrapper to ensure someone has a valid token before giving acces to method"""
        @wraps(fn)
        def decorated(*args, **kwargs):
            token = request.headers.get("token")
            if not token:
                raise InvalidTokenError("Token is missing. Please login again")
            validity = TokenService.verifyToken(token)
            if not validity[0]:
                raise InvalidTokenError(validity[1])
            return fn(*args, **kwargs)
        return decorated

    def adminRequired(fn):
        """Wrapper to ensure someone has a valid admin token before giving acces to method"""
        @wraps(fn)
        def decorated(*args, **kwargs):
            token = request.headers.get("token")
            if not token:
                raise InvalidTokenError("Token is missing. Please login again")
            if not TokenService.decodeToken(token).get("group_id") == "2":
                raise InvalidTokenError("Token is invalid. Please login again")
            return fn(*args, **kwargs)

        return decorated

    def loginUser(self):
        """Checks password to the password in the database and creates a json web token when the login is succesfull."""
        json = request.get_json()
        try:
            user = User.findUserByEmail(json["email"])
            assert EncryptionService.checkPassword(user.password, json["password"])
            token = jsonify({"token": TokenService.createJWT(user).decode("utf-8")})
            return make_response(token, 200)
        except:
            return make_response(jsonify({"message": "Login failed, please try again"}), 401)



