class Database:

    content = {"users": []}

    @classmethod
    def insert(cls, data):
        return cls.content["users"].append(data)

    @classmethod
    def remove(cls, finder):    # lambda x: x['username'] == 'Rolf'
        cls.content = [user for user in cls.content["users"] if not finder(user)]

    @classmethod
    def find(cls, finder):
        return [user for user in cls.content["users"] if finder(user)]