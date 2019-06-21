from flask_restful import Resource
from services.UserService import UserService
from services.AuthService import AuthService

class UserResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return UserService.getUser(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return UserService.updateUser(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return UserService.addUser(self, id)

class UsersResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return UserService.getAllUsers(self)

class LoginUserResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return AuthService.loginUser(self)
class UserChangePasswordResource(Resource):
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return UserService.changePassword(self)