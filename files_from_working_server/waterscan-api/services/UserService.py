from models.User import User
from services.EncryptionService import EncryptionService
from services.TokenService import TokenService
from flask_restful import reqparse
from flask import request, jsonify, make_response
from sqlalchemy import exc
from services.AuthService import AuthService


class UserService:
    # Create a parser so the JSON can be checked
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("email", type=str, required=True, help="Email cannot be left blank!")
    parser.add_argument("password", type=str, required=True, help="Password cannot be left blank!")
    parser.add_argument("name", type=str, required=True, help="Code cannot be left blank!")
    parser.add_argument("session_token", type=str, help="Session Token cannot be left blank!")
    parser.add_argument("expiration_date", type=str, help="Expiration Date cannot be left blank!")
    parser.add_argument("group_id", type=str, required=True, help="Group ID cannot be left blank!")
    parser.add_argument("waterschap_id", type=str, required=True, help="Waterschap ID cannot be left blank!")

    # This method retrieves a user
    @AuthService.tokenRequired
    def getUser(self, id):
        user = User.findUserById(id)
        if user:
            return user.json(), 201
        return {"message": "The user is not found in the database."},

    @AuthService.adminRequired
    def updateUser(self, id):
        try:
            data = UserService.parser.parse_args()
            user = User.findUserById(id)

            if user:
                user.email = data["email"]
                user.password = data["password"]
                user.name = data["name"]
                user.session_token = data["session_token"]
                user.expiration_date = data["expiration_date"]
                user.group_id = data["group_id"]
                user.waterschap_id = data["waterschap_id"]
            else:
                user = User(id, data["email"], data["password"], data["name"], data["session_token"],
                            data["expiration_date"], data["group_id"], data["waterschap_id"])
            user.save()
            return user.json()
        except exc.IntegrityError:
            return "Email already exists!"

    @AuthService.adminRequired
    def getAllUsers(self):
        return list(map(lambda x: x.json(), User.findAllUsers()))


    @AuthService.adminRequired
    def addUser(self):
        try:
            json = request.get_json()
            user = (None,
                    json["email"],
                    EncryptionService.hashPassword(json["password"]),
                    json["name"],
                    None,
                    None,
                    1,
                    1)
            user.addUser()
            return 200

        except:
            return {"message": "Login unsuccesfull, please try again"}, 403


    def getAllUsers(self):
        return list(map(lambda x: x.json(), User.findAllUsers()))

    @AuthService.tokenRequired
    def changePassword(self):
        json = request.json
        token = request.headers["token"]
        # noinspection PyBroadException
        try:
            userId = TokenService.decodeToken(token)["user"]
            user = User.findUserById(userId)
            assert EncryptionService.checkPassword(user.password, json["oldPassword"])
            assert json["newPassword"] == json["confirmPassword"]
            user.password = EncryptionService.hashPassword(json["newPassword"])
            user.save()
            return make_response(jsonify({"message": "Password changed succesfully"}), 200)
        except:
            return make_response(jsonify({"message": "password change failed, please try again"}), 401)
