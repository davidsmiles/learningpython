from user import User
from saveable import Saveable


class Admin(User, Saveable):

    def __init__(self, username, password, access_level):
        super(Admin, self).__init__(username, password)
        self.access_level = access_level

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access level': self.access_level
        }

    def __repr__(self):
        return f'<Admin {self.username} with access level: {self.access_level}>'


