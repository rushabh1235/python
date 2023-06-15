"abstractmethod"
from abc import ABC,abstractmethod # ABC,abstractclass or *
class perent(ABC):
    
    @abstractmethod
    def pname(self):
        return 0
        # pass
    
class child1(perent):
    def __init__(self,name,perent):
        self.name=name
        self.father=perent

    @staticmethod
    def permission():
        print("hello guys")
        
    def pname(self):
        return f"{self.name} {self.father}"
        
# class child2(perent):
#     def __init__(self,name,perent):
#         child1.__init__(self,name,perent)
    
#     def pname(self):
#         return f"{self.father} {self.name}" 
        
# rushabh=child1("rushabh","genmalbhai")
# rushabh.permission()
# print(rushabh.pname())
# rushabh.permission()
# sandip=child2("sandip","genmalbhai")
# print(sandip.pname())
