from admin import Admin
from database import Database

a1 = Admin('david', 'david', 3)
u1 = Admin('james', 'james', 5)

users = [a1, u1]
for user in users:
    user.save()

print(Database.content)
print(Database.find(lambda x: x['username'] == 'david'))
