class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("name",self.name)
        print("Regno",self.regno)

t1=teacher("arjun","11")
t2=teacher("regan","12")

# t1.name="arjun"
# t1.regno="11"
# t2.name="regan"
# t2.regno="12"

t1.display()
t2.display()