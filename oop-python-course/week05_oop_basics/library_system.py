class Book:
    def __init__(self, title, author, year):
        self.title_TLD = title
        self.author_TLD = author
        self.year_TLD = year

    def display_book(self):
        print("Title:", self.title_TLD)
        print("Author:", self.author_TLD)
        print("Year:", self.year_TLD)
        print()


book1 = Book("Python Programming", "John Smith", 2022)
book2 = Book("Learning OOP", "Ana Cruz", 2023)
book3 = Book("Data Structures", "Mark Lee", 2021)

book1.display_book()
book2.display_book()
book3.display_book()
