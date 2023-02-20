class Overloading:#Overload@signature()
    def getmethod(self,j):
        print("First method",j)#getMethod.overload@signature(“int”)
    def getMethod(self,i):
        print("Second method",i)
obj = Overloading()
obj.getmethod(1)
obj.getMethod(2)

