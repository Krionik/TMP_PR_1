class Strategy:
    def do(self) -> None:
        pass


class first(Strategy):
    def do(self) -> None:
        print("Мы начинаем первые!")
        print("Нет времени на повторение!")


class second(Strategy):
    def do(self) -> None:
        print("Мы начинаем вторые!")
        print("Стоит повторить план перед началом!")


class Worker:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        print('\nСмена стратегии\n')
        self.strategy = strategy

    def work(self) -> None:
        self.strategy.do()


worker = Worker(first())
worker.work()
worker.set_strategy(second())
worker.work()
