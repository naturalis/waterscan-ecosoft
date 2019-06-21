from models.UserGroup import UserGroup
from flask_restful import reqparse
from flask import request
from sqlalchemy import exc
from services.AuthService import AuthService

class UserGroupService:
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="ID cannot be left blank!")
    parser.add_argument("name", type=str, required=True, help="Name cannot be left blank!")

    @AuthService.tokenRequired
    def getUserGroup(self, id):
        usergroup = UserGroup.findUserGroupById(id)
        if usergroup:
            return usergroup.json(), 201
        return {"message": "The waterschap is not found in the database."}, 404

    @AuthService.tokenRequired
    def getAllUserGroups(self):
        return list(map(lambda x: x.json(), UserGroup.findAllUserGroups()))

    @AuthService.adminRequired
    def updateUserGroup(self, id):
        try:
            data = UserGroupService.parser.parse_args()
            usergroup = UserGroup.findUserGroupById(id)

            if usergroup:
                usergroup.id = data["id"]
                usergroup.name = data["name"]
            else:
                usergroup = UserGroup(data["id"], data["name"])

            usergroup.save()
            return usergroup.json()
        except exc.IntegrityError:
            return "Name already exists!"

    @AuthService.adminRequired
    def addUserGroup(self, id):
        try:
            data = UserGroupService.parser.parse_args()
            usergroup = UserGroup.findUserGroupById(id)

            if usergroup:
                return "The Usergroup already exists!"
            else:
                usergroup = UserGroup(data["id"], data["name"])
                usergroup.save()
                return usergroup.json()
        except exc.IntegrityError:
            return "The name already exists!"

    @AuthService.adminRequired
    def removeUserGroup(self, id):
        usergroup = UserGroup.findUserGroupById(id)
        if usergroup:
            usergroup.delete()
            return {"message": "The User Group with id '{}' is deleted!".format(id)}
        else:
            return "The User Group does not exist!"

    def getAllUserGroups(self):
        return list(map(lambda x: x.json(), UserGroup.findAllUserGroups()))