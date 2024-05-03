class ILanch:
    def make(self):
        pass


class RussianLanch(ILanch):
    def make(self):
        print('Приготовлены щи')


class ItalianLanch(ILanch):
    def make(self):
        print('Приготовлен гаспачо')


class IDessert:
    def make(self):
        pass


class RussianDessert(IDessert):
    def make(self):
        print('Приготовлена пастила')


class ItalianDessert(IDessert):
    def make(self):
        print('Приготовлена панна котта')


class IRestourant:
    def lanch(self) -> ILanch:
        pass

    def dessert(self) -> IDessert:
        pass


class RussianRestourant(IRestourant):
    def lanch(self) -> ILanch:
        return RussianLanch()

    def dessert(self) -> IDessert:
        return RussianDessert()


class ItalianRestourant(IRestourant):
    def lanch(self) -> ILanch:
        return ItalianLanch()

    def dessert(self) -> IDessert:
        return ItalianDessert()


kitchen = RussianRestourant()
kitchen.lanch().make()
kitchen.dessert().make()
kitchen = ItalianRestourant()
kitchen.lanch().make()
kitchen.dessert().make()
