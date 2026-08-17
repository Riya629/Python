class library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def Add_books(self):
        book = input("Enter the book name::")
        self.books.append(book)
        self.no_of_books += 1
        print("Book added succesfully!")
    
    def no_of_book(self):
        print(self.no_of_books)

    def show_books(self):
        for book in self.books:
            print(f"BOOKS::", book)


l = library()
while True:
    print("-----------------Welcome to library management system---------------")
    print("1. Add books")
    print("2.Get number of books")
    print("3. Print all books")

    print("4. Exit")
    choice = int(input("Enter your choice::"))
    match (choice):
        case 1:
            l.Add_books()
        case 2:
            l.no_of_book()
        case 3:
            l.show_books()
        case 4:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice!")


