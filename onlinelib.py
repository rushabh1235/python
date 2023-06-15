import time
class lib:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        
    def books(self):
        print("This books are available")
        for i in self.booklist:
            print("=>",i)
            
    def addbook(self,book):
        self.booklist.append(book)
        print("book is added at ")
        print(time.ctime())
           
    def issu(self,user,book):
        if book in self.booklist:
            print(f"{self.user} issu this {self.book} at ")
            print(time.ctime())
            self.booklist.remove(book)
        else:
            print("book is alredy issu")
            
    def returnbook(self,user,book):
        if book not in self.booklist:
            self.booklist.append(book)
            print("return  book at ")
            print(time.ctime())
        else:
            print("this book is alredy issued")

k=1       
rushabh=lib(["bhagvatgeeta","ramayan","veds","blindworld"],"RUSHABH")
while k==1:
    print("1:bookdetailes\n 2:addbook\n 3:bookissu\n 4:returnbook\n")
    choice=input("enter your choice\n")
    
    if choice=="book detailes":
        rushabh.books()
        
    elif choice=="addbook":
        book=input("enter book\n")
        rushabh.addbook(book)
            
    elif choice=="bookissu":
        user=input("enter your name\n")
        book=input("enter book name\n")
        rushabh.issu(user,book)

    elif choice=="returnbook":
        user=input("enter your name\n")
        book=input("enter book name\n")
        rushabh.returnbook(user,book)
        
    else:
        print("please choice right")
        
