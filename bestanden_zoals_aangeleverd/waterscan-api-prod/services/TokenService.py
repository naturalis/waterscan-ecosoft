import jwt
from flask import Flask, jsonify
import datetime

app = Flask(__name__)
# secret key used to verify the token
app.config["SECRET_KEY"] = "TrHp534hKYyn95VQyUb9pmZgzwCWMaghNb7PqFVeJ23mnku4PLmZ3w6PCd3XVaxvf7krsVY7"

class TokenService:

    # Decodes token using the secret
    def decodeToken(token):
        return jwt.decode(token, app.config["SECRET_KEY"])

    # creates JWT with an expiration time of 24 hours
    def createJWT(user):
        token = jwt.encode(
            {"user": str(user.id), "group_id": str(user.group_id),
             "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
            app.config["SECRET_KEY"])
        return token

    # verifies the token on changes and expiration date.
    def verifyToken(token):
        try:
            if jwt.decode(token, app.config["SECRET_KEY"]):
                return True, jsonify({"message": "Token valid"})
            return
        except jwt.ExpiredSignatureError:
            return False, jsonify({"message": "Signature expired. Please log in again."})
        except jwt.InvalidTokenError:
            return False, jsonify({"message": "Invalid token. Please log in again"})
