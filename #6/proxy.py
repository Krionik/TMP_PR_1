class DataBase:
    def __init__(self):
        self.db = {1: 'Text_1', 2: 'Text_2', 3: 'Text_3'}

    def get_data(self, number):
        return self.db[number]


class Proxy:
    def __init__(self, db):
        self.db = db

    def querry(self, number):
        if isinstance(number, int) and 0 < number < 4:
            return self.db.get_data(number)
        else:
            return 'ERROR'


db = DataBase()
proxy = Proxy(db)

print(proxy.querry(0))
print(proxy.querry('a'))
print(proxy.querry(3))
