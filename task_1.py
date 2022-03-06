# 1.Take an input from user (Name, Age, Marks).
# 1.2.Create class with _init_ method and also create a action display() to print attributes.
# 1.3.Try to use arguments and parameters with different objects.

# We take inputs from user:

n=input("Name: ")
a=int(input("Age: "))           
m=int(input("Marks: "))

#Then we create class

class Student:
    def __init__(self,n,a,m=0):      #m=0 if someone has no marks it will print out: Your marks are: 0. Also if I need to add more marks then we add * to m (self,n,a,*m). If I want to add subjects then ** to m. (self,n,a,**m)
        self.name=n            
        self.age=a             
        self.marks=m
    def display(self):
        print("Hi,",self.name)
        print("Your age is ",self.age)
        print("Your marks are ",self.marks)
        
s1=Student(n, a, m)  
s1.display()
