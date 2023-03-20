from flask_login import UserMixin

class User(UserMixin):
    pass

users = {'admin@khoj.app': {'password': 'Admin@123'}}

# class User(UserMixin):
#   id = 12345
#   username = "admin@khoj.app"
#   password = "Admin@123"

