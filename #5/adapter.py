class IRangefinder:
    def get_length(self) -> float:
        pass


class RussianRangefinder(IRangefinder):
    def __init__(self, length):
        self.length = length

    def get_length(self) -> float:
        return self.length


class AmericanRangefinder(IRangefinder):
    def __init__(self, length):
        self.length = length

    def get_length(self) -> float:
        return self.length


class AdapterForAmericanRangefinder(IRangefinder):
    def __init__(self, am_rf):
        self.am_rf = am_rf

    def get_length(self) -> float:
        return self.am_rf.get_length() * 1.61


km = 123
mi = 12

RussianRf = RussianRangefinder(km)
AmericanRf = AdapterForAmericanRangefinder(AmericanRangefinder(mi))

print(f'l_1 => {km} km, l_2 => {mi} mi')
print(f'l_1 => {RussianRf.get_length()} km, l_2 => {AmericanRf.get_length()} km')
