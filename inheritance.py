"single iheritance"
# class player:
#     com="google"
#     def __init__(self):
#         self.name="rushabh"
#         self.salary=90000
#         self.com="tcs"
#         self.id=12345
        
#     def info(self):
#         print(f"hello guys this is {self.name} and this guy play {self.salary}")

# class employee(player):
#     def __init__(self,name,salary,office):
#         self.name=name
#         self.salary=salary
#         self.office=office
#         # super().__init__()
#         player.__init__(self)
#         # print(player.com)
#         # print(super().com)
                
#     def detailes(self):
#         print(f"this is {self.name} and this guy work in  {self.office} and salary {self.salary}")    

# # rushabh=player()  
# # rushabh.info()
# sandip=employee("sandip",80000,"it")
# # print(sandip.name)
# # print(sandip.id)
# sandip.detailes()
# sandip.info()

######################################
"multiple inheritance"
class player:
    # fname="rushabh"   
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def info(self):
        print(f"hello guys this is {self.name} and earn {self.salary}")

class employee:
    # fname="sandip"
    def __init__(self):
        self.name="sandip"
        self.salary=80000
        self.office="tcs"
    
    def detailes(self):
        print(f"hello guys this is {self.name} and earn {self.salary} and hework in {self.office}")

        
class student:
    # fname="minaxi"
    def __init__(self,name,cast,collage):
        self.name=name
        self.cast=cast
        self.collage=collage
 
    def information(self):
        print(f"this is {self.name} and his cast is {self.cast} and he study in {self.collage}")    

class guy(player,employee,student):       
    def __init__(self,name,salary,office,cast,collage,classes):
        self.name=name
        self.salary=salary
        self.office=office
        self.cast=cast
        self.collage=collage
        self.classes=classes
        
        # player.__init__(self, name, salary)           #without super
        # employee.__init__(self) #without super 
        # student.__init__(self, name,cast,collage) #without super 
        def detailes(self):
            print(f"hello guys this is {self.name} and earn {self.salary} and hework in {self.office}")

        # super().__init__(name, salary)                  #use super
        # super(player,self).__init__(name,salary,office) #use super
        # super(employee,self).__init__(name,cast,collage)#use super
        
rush=player("rushabh",100000)  
# rushabh.info()    
rusha=employee()
# rushabh.detailes()
rushabh=guy("rusha",100000,"google","prajapati","silver oak university","btech")
# rushabh.info()
rushabh.detailes()
# rushabh.information()
print(rushabh.salary)

################################
"multilevel inheritance"
# class player:
    # name="rushabh"
    # game="circket" #public veriable public veriable use all class 
    # __income=200000 #private veriable private veriable use only base class
    # _tax=2300 #protected veriable protected veriabel use base class and drive class
#     def info(self):
#         print(f"my name is {self.name} and i play {self.game}")
        
# class senior(player):
#     sname="sandip"
#     sgame="tennis"
    
#     def info(self):
#         print(f"hello guys i am {self.sname} and i play {self.sgame}")
        
# class liveplayers(senior):
#     lname="riyu"
#     lgame="basketball"
    
#     def information(self):
#         print(f"i am {self.lname} and i am {self.lgame} player")
        
# rushabh=player()
# print(type(rushabh))
# rushabh.info()
# print(rushabh._player__income)
# sandip=senior()
# sandip.info()
# print(sandip.sgame)
# riyu=liveplayers()
# riyu.information()
# riyu.info()
# print(riyu._tax)