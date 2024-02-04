class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def get_book_info(self):
        return f"{self.title} от {self.author}, жанр: {self.genre}, страниц: {self.pages}"

    def read_book(self):
        return f"Ты читаешь {self.title}"

    def finish_book(self):
        return f"ты прочитал {self.title} ура"

book1 = Book("Чистый Код", "Роберт Мартин", 281, "Безысходность")
print(book1.get_book_info())
print(book1.read_book())
print(book1.finish_book())