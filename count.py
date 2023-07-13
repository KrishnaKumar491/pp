# mystr="a,a,a,b,b,b,b,b,c,c"
# mylist=mystr.split(',')
# visited=[]
# for ch in mylist:
#  if ch not in visited:
# print(f"{ch}:{mylist.count(ch)}")
# visited.append(ch)

count=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
       count=count+1
print(count)