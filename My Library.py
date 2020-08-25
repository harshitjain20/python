class Liabrary:
    def __init__(self,books,libraryName):
        self.booklist = list(books)
        self.name = libraryName
        self.landedBooks = {}
    def displayBook(self):
        print("we have the following books")
        for b in range(len(self.booklist)):
            print(f"{b}. {self.booklist[b]}")
    def addNewBook(self,book):
        self.booklist.append(book)
        print("new Book Added successfully..!!")
    def landABook(self,bookname,username):
        if bookname in self.booklist:
            if bookname not in self.landedBooks.keys():
                self.landedBooks.update({bookname:username})
            else:
                print(f"this book has already landed to {self.landedBooks[bookname]}")
        else:
            print("We dont have this book in our library")
    def removeBook(self,book):
        self.booklist.remove(book)

    def landedBooklist(self):
        print("Following books are landed to following peoples \n")
        if len(self.landedBooks)==0:
            print("No Books are landed yet...!!")
        else:
            for book,user in self.landedBooks.items():
                print(f"{book} : {user}")

if __name__ == '__main__':
    listofBooks = [
        "Python Basics",
        "python Advance",
        "C++",
        "Java",
        "PHP",
        ".Net",
        "Javascript",
        "React",
        "Angular"
    ]
    lb = Liabrary(listofBooks,"Jain Liabrary")
    while True:
        print("Select options \n")
        print("1 Display Book")
        print("2 Add Book")
        print("3 Remove Book")
        print("4 Land A Book")
        print("5 Landed Books")
        userchoice = int(input())
        if userchoice == 1:
            lb.displayBook()
        elif userchoice == 2:
            bk = input("Enter Book Name")
            lb.addNewBook(bk)
        elif userchoice == 3:
            bk = input("Enter The Book Name you want to remove")
            lb.removeBook(bk)
        elif userchoice == 4:
            name = input("Enter your name")
            bk = input("Enter the book you want")
            lb.landABook(bk,name)
        elif userchoice == 5:
            lb.landedBooklist()
        else:
            print("Invalid input...!!!! Please try again")

        uc2 = input("Do you want to continue [Y/N]")
        if uc2.lower() == "n":
            break