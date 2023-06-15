import re
# info="adc cdd ww nmnwww"
info="Database handlers aiai bibi bbbb bb bb baba create a database in ac such a way that ac only one set of software program provides access of data to all the users. The main purpose of the database is to operate a large amount of information by storing, retrieving, and managing data.There are many dynamic websites on the World Wide Web nowadays which are handled through databases. For example, a model that checks the availability of rooms in a hotel. It is an example of a dynamic website that uses a database.There are many databases available like MySQL, Sybase, Oracle, MongoDB, Informix, PostgreSQL, SQL Server, etc.Modern databases are managed by the database management system (DBMS)>SQL or Structured Query Language is used to operate on the data stored in a database. SQL depends on relational algebra and tuple relational calculus."
# info="75 erergh 2558sdg  28fg teff258e f rg2rg5522 refea25eg2sgsg4g"
# print(info.split(' '))

"meta character"
# text=re.compile(r'database')
# text=re.compile(r'.w') # . all character match
# text=re.compile(r'^Data') # which word start to string
# text=re.compile(r'calculus.$') # which word end to string
# text=re.compile(r'ba*') # start "b" and second character 0 time or more time a  
# text=re.compile(r'an+') # start "a" and second character 1 time or more time n 
# text=re.compile(r'ac{2}') # start "a" and second character how many time to you decide 
# text=re.compile(r'(ai){2}') # searching group variable
# text=re.findall(r'ac{2}|k',info) # either or
# print(text)

"special sequences"
# text=re.compile(r'\ADatabase') # all string start this word
# text=re.compile(r'\bex') # start this word
# text=re.compile(r'\d{2,}') # end this word

# info="hello this is database and in ce database is important"
# SAME=text.finditer(info)# all
# SAME=text.findall(info) # string form
# SAME=text.search(info) # only one
# SAME=text.split(info) # before and after this word
# SAME=re.finditer('w+',info)
# SAME=re.finditer('.w',info)
# SAME=re.findall('w+', info)   
# SAME=re.finditer('[^aeiou]',info)
# SAME=re.findall('ac{2}|k',info)
# info="rushabhprajapati"
# info="dv ee 122 dwd33"
# SAME=re.findall('rushabh?prajapati',info)
# SAME=re.findall('[0-9]',info)
r="rushah@gmail.com"
# SAME=re.findall('^[a-z]+?@[a-z]+\.[a-z]+$',r)
# print(SAME)
# SAME=re.finditer('\d{2,}',info) #{2},{2,4},{2,}
s=r'^[a-z]+?@[a-z]+\.[a-z]+$'
# SAME=re.match(r'h...?o|[0-9]', input())
# SAME = re.match('rush',r)
# print(SAME)
# for same in SAME:
#     print(same)

# finditer all
# findall string list form
# search one 
# split
