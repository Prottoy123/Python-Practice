class MathClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Multiply_function(self):
        z=self.x*self.y
        return z
     
firstObject=MathClass(5,10) # creating an object
 
print(firstObject.Multiply_function()) # Accessing a class function
 
firstObject.x=15 #Modifying the class property
 
print(firstObject.Multiply_function()) # Accessing a class function after modifying the class property
