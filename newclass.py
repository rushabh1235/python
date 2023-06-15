class family:
    cast="prajapati" #class veriable
    member=6

    "it's called constroctor"
    # def __init__(self): 
    #     self.name="sandip"
    #     self.wifename="ramila"
    #     self.sonname="riyansh"
     
    def __init__(self,name,earn,office):
        self.name=name
        self.earn=earn
        self.office=office
       
    @classmethod 
    def info(cls,String):
        return cls(*String.split(','))
        
        
    "regular method" 
    def relationship(self):
        print(f"{self.name} is ....")
    
    "class method"
    # @classmethod    
    # def change(cls):
    #     cls.cast="marvadi"
    #     cls.member=6
    
    "static method"
    @staticmethod
    def regular():
        print("hello rushabh") 
    
"object  class"
# rushabh=family()
# print(rushabh.cast)
# print(rushabh.member)

# sandip=family() #you define object so dairect called constroctor
sandip=family("sandip","20000","charchit")
# rushabh=family.info("rushabh,80000,tcs")
# print(rushabh.office)
# print(sandip.name)    
# print(sandip.earn)
# family.cast="marvadi"
# sandip.relationship()
# print(sandip.wifename)
# print(sandip.sonname)

# family.change() #or sandip.change()
# print(sandip.cast)
# print(family.cast)

# sandip.regular()
# family.regular()

"""if you wil create class and create function in class so always in class arguments self is compulsory but in static function self not requered"""