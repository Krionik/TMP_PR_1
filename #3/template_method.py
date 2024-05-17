class Book:
    def make(self) -> None:
        self.sketch_out_plot()
        self.add_annex()
        self.select_circulation()

    def sketch_out_plot(self) -> None:
        pass

    def add_annex(self) -> None:
        pass

    def select_circulation(self) -> None:
        pass


class Writer:
    def __init__(self, book: Book):
        self.book = book

    def set_book(self, book: Book):
        print('\nПоменять книгу\n')
        self.book = book

    def make_book(self):
        self.book.make()


class makeFantasticBook(Book):
    def sketch_out_plot(self) -> None:
        print('Придумать фантастический сюжет')

    def add_annex(self) -> None:
        print('Добавить карту придуманного мира')

    def select_circulation(self) -> None:
        print('Тираж: 15000')


class makeDetectiveBook(Book):
    def sketch_out_plot(self) -> None:
        print('Придумать запутанный детективный сюжет')

    def add_annex(self) -> None:
        print('Добавить в приложение всех действующих лиц')

    def select_circulation(self) -> None:
        print('Тираж: 10000')


writer = Writer(makeFantasticBook())
writer.make_book()
writer.set_book(makeDetectiveBook())
writer.make_book()
