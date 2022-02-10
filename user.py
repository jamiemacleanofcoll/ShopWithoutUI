import datetime
from enum import Enum


class Role(Enum):
    ADMIN = 0
    USER = 1


class User:
    user_id: int
    firstname: str
    lastname: str
    date_of_birth: datetime
    username: str
    password: str
    role: Role

    def __init__(self, user_id, firstname, lastname, date_of_birth, username, password, role):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password
        self.role = role

    def change_attribute(self, key, value):
        if key == "firstname":
            self.firstname = value
        elif key == "lastname":
            self.lastname = value
        elif key == "date of birth":
            self.date_of_birth = value
        elif key == "username":
            self.username = value
        elif key == "password":
            self.password = value
        else:
            raise ValueError


