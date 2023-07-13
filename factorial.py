# num=int(input("enter the value :"))
factorial=1
num=5
if num<0:
    print("negative not exist")
elif num==0:
    print("the factorial is :1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of ", num, "is",factorial)
