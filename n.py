n=int(input('n:'))
if n%2==0:
    if (n>=0 or n<=5 ):  
        print('not weired')
    elif(n>=6 or n<=19):
        print('weired')
    else:
        print('not weired')    
else:
    print('weired')