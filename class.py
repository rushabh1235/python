class office:
    cast="prajapati"
    def detailes(self):
        print(f"hello guys my name is rushabh and i work in {self.office} and i earn {self.salary}")

rushabh=office()
rushabh.salary=80000
rushabh.office="google"
rushabh.position="CEO"
print(rushabh.position)
print(rushabh.cast)
print(office.cast)
rushabh.detailes()

class family:
    cast="prajapati"
    income=80000000000
    def __init__(self,rname,sname,relation): #constroctor
        self.rname=rname
        self.sname=sname       
        self.rsrelation=relation        
    
    @classmethod
    def new(cls,cast):
        cls.newcast=cast      
    
    @staticmethod
    def name():
        print("hello rushabh")    
    
    @classmethod
    def relation(cls,rname,sname,rsrelation):
        return cls(rname,sname,rsrelation)       
    
    def ans(self):
        print(f"{self.rname} and {self.sname} is {self.rsrelation}")
        
member=family("rushabh","sandip","brothers")
print(member.rrname)
memb=family.relation("sandip","ramila","cuppel")
memb.ans()
print(member.name)
family.name()
print(family.cast)
family.new("marvadi") #also access instance as member.new("marvadi")
print(family.newcast)

class family:
    cast="prajapati"
    income=80000000000
    def __init__(self,rname,sname,relation): #constroctor
        self.rrname=rname
        self.name=sname       
        self.rsrelation=relation        
        
    @classmethod
    def new(cls,string):
        return cls(*string.split(','))
        # rr=string.split(',')
        # return cls(rr[0],rr[1],rr[2])

# member=family("rushabh","sandip","80000")
member=family.new("rushabh,sandip,brothers")
print(member.rrname)

class sum:
    def __init__(self,a,b):
        self.r=a
        self.b=b
    
    def __add__(self, other):
        x=self.r+other.r
        y=self.b+other.b
        return sum(x,y)
    
    def __mul__(self, other):
        x=self.r*other.r
        y=self.b*other.b
        return (x,y)
    
    def __eq__(self, other):
        x=self.r == other.r
        y=self.b == other.b
        return (x,y) 
    
    def __str__(self):
        return f"hello {self.r} {self.r}"
    
s=sum(10,12)
v=sum(10,12)
print(s+v)
p=s+v
print(p.b)
s=sum("rushabh")
v=sum("prajapati")
print(s+v)
print(s*v)
print(s==v)
print(s)