import math
import itertools
 
# Function to check
# Log base 2
def Log2(x,n):
    if x == 0:
        return false;
 
    return (math.log10(x) /
            math.log10(n));
 
# Function to check
# if x is power of 2
def Powi(num, power):
    float_candidate = num ** (1/power)
    for int_candidate in itertools.count(int(math.floor(float_candidate))):
        powered = int_candidate ** power
        if powered == num: return 1
        elif powered > num: return 0
def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result 
def sub_lists (l): 
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists 
          
    return lists 
def persq(number):
    per=90
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        #print(number, "is a perfect square")
        per=1
    else:
        #print(number, "is not a perfect square")
        per=0
    return per
def gimmelist(d,e):
    cheese=[]
    n=d+1
    while n<e:
        cheese.append(n)
        n=n+1
    return cheese
def check(b,c,k):
    butter=gimmelist(b,c)
    pie=sub_lists(butter)
    i=0
    conclusion=98
    while i<int(len(pie)):
        moon=pie[i]
        prodi=multiplyList(moon)
        phew = b*c*prodi
        omg = Powi(phew,k)
        if omg==1:
            conclusion=1
            break
        else:
            conclusion=0
            i=i+1
    return conclusion 
           
def hola(a,pika):
    worker=a+1
    while 1>0:
        omega = check(a,worker,pika)
        if omega == 1:
            theans=worker
            break
        else:
            worker=worker+1
    return theans

A=int(input("Value of N in F_N(x): "))
B=int(input("Value of x in F_N(x): "))
print("F_"+A+"("+B+")=",hola(B,A))
