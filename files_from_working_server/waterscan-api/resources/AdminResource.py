from services.AdminService import AdminService
from flask_restful import Resource
from services.AuthService import AuthService

class AdminResource(Resource):
    @AuthService.adminRequired
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return AdminService.createUser(self)

    @AuthService.adminRequired
    def put(self):
        """PUT request for this resource layer passes it to service layer"""
        return AdminService.updateUser(self)

    @AuthService.adminRequired
    def delete(self):
        """DELETE request for this resource layer passes it to service layer"""
        return AdminService.deleteUser(self)

class AdminResetResource(Resource):
    @AuthService.adminRequired
    def post(self):
        """POST request for this resource layer passes it to service layer"""
        return AdminService.resetPassword(self)