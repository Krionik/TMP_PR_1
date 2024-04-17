class Manager:
    def recommend(self, _client: 'Client'):
        pass


class Client:
    def getType(self):
        pass

    def suggested(self, _manager: Manager):
        pass


class Child(Client):
    def getType(self):
        return 'Ребёнок'

    def suggested(self, _manager: Manager):
        _manager.recommend(self)


class YoungMan(Client):
    def getType(self):
        return 'Молодой человек'

    def suggested(self, _manager: Manager):
        _manager.recommend(self)


class OldMan(Client):
    def getType(self):
        return 'Пожилой человек'

    def suggested(self, _manager: Manager):
        _manager.recommend(self)


class ClothingSalesman(Manager):
    def __init__(self):
        self.offer = ''

    def recommend(self, _client: Client):
        if isinstance(_client, Child):
            self.offer = 'предложить шапку с ушками'
        elif isinstance(_client, YoungMan):
            self.offer = 'предложить модную куртку'
        elif isinstance(_client, OldMan):
            self.offer = 'предложить тёплый свитер'


clients = [Child(), YoungMan(), OldMan()]
manager = ClothingSalesman()

for client in clients:
    client.suggested(manager)
    print(client.getType() + ':', manager.offer)
