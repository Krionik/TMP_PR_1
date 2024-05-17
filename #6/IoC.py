class ServerLocator:
    def __init__(self):
        self.services = dict()

    def getService(self, name):
        return self.services.get(name, None)

    def addService(self, service):
        if type(service) not in self.services:
            self.services[type(service)] = service
        else:
            print('Exist!')

class ClassA:
    def do(self): {print('class_A')}
class ClassB:
    def do(self): {print('class_B')}
class ClassC:
    def do(self): {print('class_C')}


a, b, c, c1 = ClassA(), ClassB(), ClassC(), ClassC()

locator = ServerLocator()
locator.addService(a)
locator.addService(b)
locator.addService(c)
locator.addService(c1)

locator.getService(ClassA).do()