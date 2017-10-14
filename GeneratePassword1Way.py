import random
def Strongpass():
    c = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s = "".join(random.sample(s1,4))
    n = int(random.randrange(101,300,2))
    pass1 = c+s+"@"+str(n)
    return(pass1)

def Weakpass():
    c = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n = int(random.randrange(10001,30000,1))
    pass2= c+str(n)
    return(pass2)
print("1:Weak password")
print("2:Strong password")
n = int(input("Enter Your choice:-"))
if(n==1):
    print(Weakpass())
elif(n==2):
    print(Strongpass())    
    
        
        
    
    