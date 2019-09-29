from oop.advanced_oop.admin import Admin
from oop.advanced_oop.database import Database

a1 = Admin('david', 'david', 3)
u1 = Admin('james', 'james', 5)

users = [a1, u1]
[user.save() for user in users]

print(Database.find(lambda x: x['username'] == 'david'))
Database.remove(lambda x: x['username'] == 'david')
print(Database.content)
