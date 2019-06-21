from flask import request, jsonify, make_response
from services.EncryptionService import EncryptionService
from models.User import User
from random import randint

class AdminService:
    def createUser(self):
        """Logic to create a new user"""
        json = request.get_json()
        user = User(None, json["email"], EncryptionService.hashPassword(json["password"]), json["name"],
                    None, None, json["group_id"], json["waterschap_id"])
        user.addUser()
        return make_response(jsonify(user.json()))

    def updateUser(self):
        """Logic to update data of an user"""
        try:
            json = request.get_json()
            user = User.findUserById(json["id"])
            user.email = json["email"]
            user.name = json["name"]
            user.group_id = json["group_id"]
            user.waterschap_id = json["waterschap_id"]
            user.updateUser()
            return make_response(jsonify({"message": "Update on user with ID " + str(json["id"]) + " succesfull"}),
                                 200)
        except:
            return make_response(jsonify({"message": "Update on user with ID " + str(json["id"]) + " unsuccesfull"}),
                                 500)

    def deleteUser(self):
        """Logic to delete a user"""
        try:
            json = request.get_json()
            user = User.findUserById(json["id"])
            user.removeUser()
            return make_response(jsonify({"message": "User with id: " + str(user.id) + " removed succesfully"}), 200)
        except:
            return make_response(jsonify({"message": "delete unsuccesfull"}), 500)

    def resetPassword(selfs):
        """Logic to reset a users password"""
        json = request.get_json()
        user = User.findUserByEmail(json["email"])
        pin = str(randint(0, 9999))
        user.password = EncryptionService.hashPassword(pin)
        user.save()
        return make_response(jsonify({"pin": pin}))
