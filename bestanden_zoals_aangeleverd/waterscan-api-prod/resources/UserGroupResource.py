from flask_restful import Resource
from services.UserGroupService import UserGroupService

class UserGroupResource(Resource):
    def get(self, id):
        """GET request for this resource layer passes it to service layer"""
        return UserGroupService.getUserGroup(self, id)

    def put(self, id):
        """PUT request for this resource layer passes it to service layer"""
        return UserGroupService.updateUserGroup(self, id)

    def post(self, id):
        """POST request for this resource layer passes it to service layer"""
        return UserGroupService.addUserGroup(self, id)

    def delete(self, id):
        """DELETE request for this resource layer passes it to service layer"""
        return UserGroupService.removeUserGroup(self, id)

class UserGroupsResource(Resource):
    def get(self):
        """GET request for this resource layer passes it to service layer"""
        return UserGroupService.getAllUserGroups(self)