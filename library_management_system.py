class Library:
    def __init__(self, name):

        self.name = name
        self.books = []

        def add_book(self, book_name):

            self.books.append(book_name):
            print(f' "{book_name}" added to the library')

            def show_books(self):

                if self.books:
                    print(f"\n Books available in {self.name}:")
                    for book in self.books:
                        print(f"- {book}")

                    else:
                        print("No boooks in the library!")

                     def borrow_book(self, book_name):

                    if book_name in self.books:
                        print(f'You biorrowed "{book_name}". Enjoy!')
                    else:
                        print(f'Sorry... "{book_name}"is not available over here...')

            # Create a library object
            my_library = Library("Kids Library")

            # Add books
            my_library.add_book("Harry Potter")
            my_library.add_book("Alice in Wonderland")
            my_library.add_book("Charlie and the Chocolate Factory")

            #Show available books
            my_library.show_books()

            # Borrow a book
            my_library.borrow_book("Alice in Wonderland")
            
            # show updates book list
            my_library.show_books()

                       

