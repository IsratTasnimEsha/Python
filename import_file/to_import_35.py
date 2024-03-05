#BISMILLAHIR RAHMANIR RAHIM

def lcm(num1, num2):
    lcm=max(num1, num2)
    while(lcm%num1!=0 or lcm%num2!=0):
        lcm+=1
    return lcm

def swap(x, y):
    x, y= y, x
    return x, y