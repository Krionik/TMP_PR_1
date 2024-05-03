class IMediator:
    def notify(self, actor: 'Actor', message: str):
        pass


class Actor:
    def __init__(self, _mediator: IMediator):
        self._mediator = _mediator

    def set_mediator(self, med: IMediator):
        self._mediator = med


class Courier(Actor):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__is_deliver = False

    def execute_work(self):
        print('Курьер доставляет товар')
        self._mediator.notify(self, 'Курьер в пути...')

    def set_work(self, state: bool):
        self.__is_deliver = state
        if state:
            print('Курьер освободился')
        else:
            print('Курьер занят')


class Director(Actor):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__text: str = ''

    def give_command(self, cmd: str):
        self.__text = cmd
        if cmd == '':
            print('Директор уведомлён о том, что курьер в пути')
        else:
            print(f'Директор дал команду: {cmd}')
        self._mediator.notify(self, cmd)


class System(IMediator):
    def __init__(self, _courier: Courier, _director: Director):
        self.__courier = _courier
        self.__director = _director
        _courier.set_mediator(self)
        _director.set_mediator(self)

    def notify(self, actor: 'Actor', message: str):
        if isinstance(actor, Director):
            if message == '':
                self.__courier.set_work(False)
            else:
                self.__courier.set_work(True)
        if isinstance(actor, Courier):
            if message == 'Курьер в пути...':
                self.__director.give_command('')


designer = Courier()
director = Director()

mediator = System(designer, director)

director.give_command('Доставка чайника')
print()
designer.execute_work()
