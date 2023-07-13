class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("name",self.name)
        print("Reg no",self.regno)

s1=student()
s2=student()
s1.name="krishna"
s1.regno="26"

s2.name="lokesh"
s2.regno="27"

s1.display()
s2.display()   
