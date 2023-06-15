# import argparse
# import sys
# # print(dir(sys))
# print(len(sys.argv))
# print(str(sys.argv)) 
# print(sys.argv[0])   
  

def cal(args):
    if args.a=='add':
        return args.r+args.k
    elif args.a=='sub':
        return args.r-args.k
    elif args.a=='mul':
        return args.r*args.k
    elif args.a=='div':
        return args.r/args.k
    elif args.a=='mod':
        return args.r%args.k
    
parser=argparse.ArgumentParser()
parser.add_argument("--r",type=int,default=0)
parser.add_argument("--k",type=int,default=0)
parser.add_argument("--a",type=str,default=0)

args=parser.parse_args()
sys.stdout.write(str(cal(args)))

# import argparse
# import sys 
def leap(arg):
    if arg.y%4==0:
        return "year is leap year"    
    else:
        return "this year is not lepa year"
# parser=argparse.ArgumentParser(description="leap year program")
# parser.add_argument('--a',type=str,default='rushabh',help="enter name")
parser.add_argument('--y',type=int,default=2022,help='enter year')
# parser.add_argument('--l',type=str)

# arg=parser.parse_args()
# sys.stdout.write(str(leap(arg)))