#Second way to Generate Password
import random
def Strongpass(n):
    s1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@$&%#*0123456789'
    s = "".join(random.sample(s1,n))
    return(s)

n =int(input("how many character password You want="))
print(Strongpass(n))