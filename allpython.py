"""what is python language interpreted or compiled:=>

		1) python is neither true compiled time or not pure interpreted language.but it is called interpreted language
		2) (.py) source code is first compiled to byte code as (.pyc)
		3)this byte code (.pyc) can be interpreted  

		==>python is a computer programming language used to build a website,software and also used in ML,DL, and data anaylitics.
		==>and python is interprited oop and high level programimng language.
		in python interprited means source code of python program convert into byte code and than executed by the python vertual machine

command line argument:=>
	import sys
	print(len(sys.argv))   
	print(sys.argv[0])   # first value of argv is file name

data type in python: 
			1)number:
				1)int =>range is not fixed in python they use all the memory is available
				2)float => range of float in python is 8 Byte
				3)complex number: complex(1,2)=>1+2i
				4)bool
			2)string
			3)list
			4)tuple
			5)dictionary


POP(Procedure Oriented Programming) : 
					POP is a programming model in which we can divide programm in to a functions..

					it is top down approch.

					pop not give importance to data but it gives importance to function as well as sequence of actions.


OOP(Object Oriented Programming) :
					oop is required to impliment real world entitys..

					OOP prograamm is associated whith the concept of class,object and various other concept like abstraction,data hiding,polimorpism,inheritance...
					
					object: object is real world physical entity which have state and behaviour..
						ex: for banking system object state is data of object and behaviour is withdraw money etc..
						ex: let car is object then state is staring wheel,seets etc and behaviour is functionality of car ex breaking the car move the car etc..
					
					class: class is a logical entity for example it is collection of objects class contain member functions and data members... 

		note for oop:=>		inhritence:->inhritance allow us to  define a class that inherit all the methods and propertice from another class
							in inheritance perent class is also called base class and child class is also called direved class
       						1)single:
							2)multiple:
							3)multilevel:
							4)hirearchi: b ,c,d inherite class a
							5)hybrid: combination of two inheritance is called hybrid inheritance
 					
********************************************************************************************************************************************************************************************
NOTE:-> FOR SORTING STRING THERE IS ONE FUNCTION ..... =>>> SORTED(STRING NAME)  (THIS FUNCTION RETURN LIST )	

note:->
	stra=input("enter word: ")
	print(f"hello world {stra}")

r:-> print("hello \namaste")=> hello
			       maste
     print(r"hello \namaste")=>hello \namaste

=> how to print double quotes text: 

print("hello \"\\nhow\" are you")
hello "\nhow" are you
**************************binary to decimal or vise versa*********************************

a="{:032b}".format(10)
print(a)
#here 32b means it give 32 bit binary number and append 0 on extra place

print("{:032x}".format(10))
#print hexadecimal  number

print("{:032o}".format(10))
#print octal no

h="%x" % (64)
print(int(h,16))
# hexadecimal to decimal


*********************************************************************************************************************************************************************************************
note:->
*********  for finding aasci value of character
	   ord("character")=> it gives aasci value of char
	
	   fro finding character from aasci value
	   chr(number)=> it gives character

********************************************************************************************************************************************************************************************
point 1: increment operator is not supported in python

point 2: python support both procedure oriented and object oriented programming

point 3: python is interpreted aswell as compiled language programming languege

point 4: when interprete python file .pyc file is created 

point 5: python doesn't support any access modifiere(private ,protected etc..) so it doesn;t provide data leval sequrity but it provide application leval security

point 6: data type: int,string,boolien

point 7: data structure : 1) list  2)tuple 3)set 4)dictionary

1)list: 
	1) indexing allowed,mutable
 	2) ordered element
	3) we can add or remove data by using index or function
	4) duplication allowed

2)tuple:
	1) indexing allowed,immutable
	2) ordered element
	3) we can add or remove data by using function only
	4) duplication allowed

3)set:
	1)indexing not allowed,mutable but frozenset is immutable
	2) unoredered element
	3) we can add data by using function only
	4) duplication not allowed
	5)in this set ele are always sorted order (only for int)
	6)if we add ele in set so always eles are added front side add pop also
 
4)dictionary:
	1) indexing by using key elment(dictionary is combination of key and value),mutable
	2) ordered element
	3)we can add by data using fun and key
	4)duplicate key is not allowed

point 8: file is used to store the permanant output of the programm

functions in file:	
	1) readlines: this function read all lines from file and store in the list line by line
	2) readline:this function read one line from file 
	3) read: this function readall file 
	
	4) writelines:this function write list in file line by line
	5) writeline:this function write one line in file
	6) write:this function write data in file
	
	7)seek(offset,wence):
		offset:it represent the from which no of character you want to start pointer
		whence: 0:start of file  1:current position  2:end of file

note:-> if we use offset then whence is always 0
	if we use whence then offset is always 0

point 9: list function:
	1) max,min
	2) extends
	3) sort
	4) index
	5) insert(index,value)
	6) pop(index)
	7) reverse
	8) remove(elemnt name)
	9) count(element name)
	10)list[strating index:ending index:jump]:=>same as string work
	11)reversed(listname or tuple namr etc...) => this function return object so write in that way ex print(list(reversed(name of datastructure)))
imp fun:-> 
	10)in and not in : if (item1) in (iitem2) :=>return true if item1 is in itwm2
	11)is and is not : if type(x) is int :=>return true if type of x is int

point 10: dictionary function:
	1) get(key name) : it gives value of key
	2) fromkeys(list name): it create dictionary by using keys of list value and value of dict is set to null
	3) keys , values : it create list and store key or value in this list
	4) items : it create list and in this list create tupple for perticular key and value
	5) update : join two dictionary
	6) clear : clear dictionary
	7) copy : copy one dict to another


point 11: annonymus function:
		1) a function which have no name is called annonymous function or lambda function
		2) lambda is not the name of function it is python keyword to represent annonymus function

#lambda function: =>

	name=lambda x: x*2
	name(5)
	# output 10
	
	name=lambda x,y:x+y
	name(1,2)
	#output 3

	li1=[1,2,3]
	li=list(map(lambda x: x+1,li1))
	#output li=[2,3,4]
	
	# map function return list of all return value by the lamda function,tuple etc
	# map fun require two argument
	
	li1=[1,2,3]
	li=list(filter(lambda x:x%2==0,li))
	print(li)
	# output li=[2]
	
	# filter function return the list of values which satisfy the condition in lamda function

	from functools import reduce
	a=(1,2,3)
	li3=reduce(lambda x,y:x+y,li+y)
	print(li3)

	#reduce function perform repeted operation over the data for ex used to add all value of list
	#this reduce function is part of functools module


*********************************************************************************************************************************************************************************************
		

point 12: some random functions:::===>>>
			
			1)random.random():=> this function generates random float no beetween 0.0 to 1.0
			2)random.randint():=>this function returns a random integer between the specified integers
			3)random.randrange():=>returns a randomly selected element from range created by start stop and jump argument.jump is allo in only this fun random.randrange
			4)random.choice():=>return randomly selected element from non empty sequence ex:random.choice("abcde")=> output: c
			5)random.suffle():=>this fun randomly reorder the element in a list. ex:random.shuffle([1,2,3,4,5])=>output:[4,2,3,1,5]

	
#####.....IMPORT RANDOM.....#####

li=[1,2,3,4,5]
print(random.randint(0,10))

print(random.choice(li))

random.shuffle(li)
print(li)

print(random.random())

print(random.randrange(1,100))


********************************************************************************************************************************************************************************************

exception handling:=>it is used for give run time error to user in non technical msg 
			also it used when you dont want to end the program at any runtime error

		BaseException class is main Exception class=>IndexError class,ValueError class etcc
		BaseException class contain indexerror,value error etc classs
		BaseException class is parent of all exception class

encaptulation:
		it means encaptulate data so we can not modified or access out side the class
		ex: __private =>put two underscore to pre variable create variable protect so you can not access variable out side of class
				but actually it is not protected variable it is ""naming convntion"" you can access this variable by doing
				=> _classname__private
polimorphism:
		it means you can run block of code on behalf of input of the program(run time)
		polimorphism means ablity to take verious form

REGULAR EXPRESSION:==>
			import re(where re is regular expression module
			
	method:=>
		1)findall=>return list of all mathches value.
			ex: print(re.findall("regular_expression","input_string"))=>return list of matching value
		
		2)search=>return starting and ending index of first matching value in term of object
				so you need to print(var_name.span()) #if not matching then return none so condition is false
			ex: var=re.search("regular_expression","input_string",flag)
			print(var.span())
		
		3)match=>return match object if starting char or word is match with re
				other wise return none
				ex: var=re.match("regular_expression","input_string",flag)

..............................................................................................
#SEARCH and MATCH both are same only difference is search find matching re index from entire list
	while match only work when starting of string is match with re

note:=>
import string

li=string.ascii_lowercase
print(li)

#it will give a to z in string formate
..............................................................................................

		4)split=>return list where string has been split at each match

		5)sub=>re.sub("regular_expression","string you want to replace","input_string","no of changes you want")
			ex:s="hello it is cat and it is nice"
				print(re.sub("(is)","was",s,1))=>hello it was cat and it is nice
				print(re.sub("(is)","was",s,2))=>hello it was cat and it was nice
 


	flags:=>
		re.I:
		Performs case-insensitive matching.	
		
		re.M:
		Makes $ match the end of a line

	
	NOTE: => SOME RE EXAMPLE HOW IT MATCHS WITH STRING:=>
	
	1	
	[Pp]ython

	Match "Python" or "python"

	2	
	rub[ye]

	Match "ruby" or "rube"

	3	
	[aeiou]

	Match any one lowercase vowel

	4	
	[0-9]

	Match any digit; same as [0123456789]

	5	
	[a-z]

	Match any lowercase ASCII letter

	6	
	[A-Z]

	Match any uppercase ASCII letter

	7	
	[a-zA-Z0-9]

	Match any of the above

	8	
	[^aeiou]

	Match anything other than a lowercase vowel

	9	
	[^0-9]

	Match anything other than a digit



	1	
	.

	Match any character except newline

	2	
	\d

	Match a digit: [0-9]

	3	
	\D

	Match a nondigit: [^0-9]

	4	
	\s

	Match a whitespace character: [ \t\r\n\f]

	5	
	\S

	Match nonwhitespace: [^ \t\r\n\f]

	6		
	\w

	Match a single word character: [A-Za-z0-9_]

	7	
	\W

	Match a nonword character: [^A-Za-z0-9_]

	Repetition Cases
	Sr.No.	Example & Description
	1	
	ruby?
	
	Match "rub" or "ruby": the y is optional

	2	
	ruby*

	Match "rub" plus 0 or more ys

	3	
	ruby+

	Match "rub" plus 1 or more ys

	4	
	\d{3}

	Match exactly 3 digits

	5	
	\d{3,}

	Match 3 or more digits

	6	
	\d{3,5}

	Match 3, 4, or 5 digits	




	re.compile:=>we can combine a regular expresion pattern into pattern object which can be used for pattern matching.
			it also helps to search a pattern again without rewriting

			ex: 	import re
				pattern=re.compile(r"(a,b,c)")
				result=pattern.findall("hello ajay how are you")
				print(result)
		
			output: ["ajay","are"]



	iterator =>for i in finditer("regular_expression","input_string"):
			s=i.span()
			print(s)
		#i.start()=>it gives starting index of matching element
		#i.end()=>it gives ending index of matching element
		#finditer("regular_expression","input_string"): this return starting and ending index of matching value


extra notes: 
		example:
			tup=(1,2,3)
			new_tuple=tup,4,5
			print(new_tuple)
		output:
			((1,2,3),4,5)

.....................

		example:
			True*True=1
			True*False=0
			False*False=0
		
.....................
		b=list(map(int,["10","22"]))
		output=> [10,20]
		a,b=map(int,["1","2"])
		output=> a=1,b=2
		map is used to map or convert type

......................
		import math
		print(math.gcd(10,20))
		math.gcd()=>gives gcd of only two no

......................
		li1=[1,2],li2=[1,2]
		li1+li2=>[1,2,1,2]


IMP:=>................
=> eval() inbuilt function in python:
	it will used to evaluate string for example
		print("1+2*3*(3+3)")=>output: 1+2*3*(3+3)
		print(eval(1+2*3*(3+3)))=>output: 37
	
	ex=>a=x+2*x
	print(a)=>x+2*x
	x=10
	print(eval(a))=>30

strong number:
Strong number is a number whose sum of all digits' factorial is equal to the number 
'n'. ... So, to find a number whether its strong number, we have to pick every digit 
of the number like the number is 145 then we have to pick 1, 4 and 5 now we will find 
factorial of each number i.e, 1! = 1, 4! = 24, 5! = 120

auto morphic number:
n mathematics, an automorphic number is a number whose square "ends" in the 	same digits as 
the number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, 
so 5, 6, 76 and 890625 are all automorphic numbers.

harshad number:
In recreational mathematics, a harshad number in a given number base, is an integer that is 
divisible by the sum of its digits when written in that base. Example: Number 200 is a 
Harshad Number because the sum of digits 2 and 0 and 0 is 2(2+0+0) and 200 is divisible by

abandant number:
https://www.geeksforgeeks.org/abundant-number/



this code usefull to get input user write on concol 
ex:
input:      input:
1           10
2           20
3           30
4
5

output:     output:
1           10
2           20
3           30
4
5

here you dont know how many number user write so use this method
import sys
=> li=sys.stdin.readlines()
for i in li:
    print(fun(int(i)))   # i contail value like '1\n' so convert in int so value is 1 """
