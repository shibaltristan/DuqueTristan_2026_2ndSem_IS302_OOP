class Booktld:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_booktld(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print()

book1tld = Booktld("Python Programming", "John Smith", 2022)
book2tld = Booktld("Data Science Basics", "Jane Doe", 2021)
book3tld = Booktld("Web Development", "Mike Johnson", 2023)

book1tld.display_booktld()
book2tld.display_booktld()
book3tld.display_booktld()
