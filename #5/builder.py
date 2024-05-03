class House:
    def __init__(self):
        self.data = ''

    def about(self):
        return self.data

    def append_data(self, info):
        self.data += f'{info}; '


class IBuilder:
    def create_walls(self):
        pass

    def create_roof(self):
        pass

    def create_windows(self):
        pass

    def get_house(self) -> House:
        pass


class Red_Builder(IBuilder):
    def __init__(self):
        self.house = House()

    def create_walls(self):
        self.house.append_data('красные стены')

    def create_roof(self):
        self.house.append_data('красная крыша')

    def create_windows(self):
        self.house.append_data('красные стёкла')

    def get_house(self) -> House:
        return self.house


class Blue_Builder(IBuilder):
    def __init__(self):
        self.house = House()

    def create_walls(self):
        self.house.append_data('голубые стены')

    def create_roof(self):
        self.house.append_data('голубая крыша')

    def create_windows(self):
        self.house.append_data('голубые стёкла')

    def get_house(self) -> House:
        return self.house


class Director:
    def __init__(self, builder):
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def build_house(self):
        self.builder.create_walls()
        self.builder.create_roof()
        self.builder.create_windows()
        print(self.builder.get_house().data)


builder_1 = Red_Builder()
builder_2 = Blue_Builder()

director = Director(builder_1)
director.build_house()

director.set_builder(builder_2)
director.build_house()
