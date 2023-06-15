class student:
    def __init__(self):
        self.name="rushabh"
        self.sem=4
        self.s="asa"
    
    def into(self):
        print(f"{self.name} prajapati")    
        
class teach(student):
    def __init__(self):
        self.name="pina"
        self.sem=8  
        super().__init__()
        # student.__init__(self)  
        
    def into(self):
        print(f"{self.name} khumbhar")    
        
s=student()
t=teach()
t.into()

# class bro:
    # __name="rushabh"
    
    # def __init__(self):
    #     self.__print()
    #     pass
    # def ans(self):
    #     self.__print()
    
    # def print(self):
    #     print(self.__name)
        
# b=bro()
# b.print()
# print(b._bro__name)

# class stu:
#     def __init__(self,name,branch):
#         # self.__name=name      private
#         # self.__branch=branch
#         self.name=name
#         self.branch=branch
    
#     def setname(self,name):
#         # self.__name=name
#         self.name=name
        
#     def getname(self):
#         # return self.__name
#         return self.name
    
#     def print(self):
#         print(f"this is {self.__name} and branch is {self.__branch}")
        
# s=stu("rushabh","CE")
# s.setname("sandip")
# print(s.getname())
# print(s._stu__name)   
        
