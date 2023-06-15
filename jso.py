import json
####### python ==> json (dumps)
# convert python object to json to use dumps
# d1={'name':'rushabh','branch':'computer engineering','university':'silver aok','sem':4,'result':True}
# print(json.dumps(d1,separators=(";","=")))
# print(json.dumps(d1, separators=("&","*")))
# print(json.dumps(d1,indent=2))
# print(json.dumps(d1))
# with open("rushabh.json","w") as r:
#     json.dump(d1,r)    
# print(d1["name"])

####### json ==> python (loads)
# convert json to python object to use loads
d1='{"name":"rushabh","branch":"computer engineering","university":"silver aok","sem":4,"result":true}'
print(d1)
# print(d1["branch"])
p=json.loads(d1)
print(p)
# with open("rushabh.json","r") as k:
#     r=json.load(k)
#     print(r)
# print(p["branch"])
# print(dir(json))

# import json
# class stu:
#     def __init__(self,name,collage,sem):
#         self.name=name
#         self.collage=collage
#         self.sem=sem
        
# rudi=stu("rushabh","ASOIT",4)

# def convert(obj):
#     if isinstance(obj,stu):
#         return {'name':obj.name,'collage':obj.collage,'sem':obj.sem}
#     else:
#         raise TypeError("Object of type stu is not JSON serializable")

# jso=json.dumps(rudi,default=convert)
# print(jso)