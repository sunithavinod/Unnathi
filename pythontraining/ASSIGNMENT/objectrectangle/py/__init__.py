
class sides:
#def area(sides):
    #s=(a+b+c)*0.5
    #return float(s*(s-a)(s-b)(s-c))**0.5
#print('area of triangle',area)
    
    
    
    class triangle(tri):
    def get_area(tri):
        s = (tri.a + tri.b + tri.c) / 2
        return float((s*(s-self.a)*(s-self.b)*(s-self.c))) ** 0.5        

a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
t = triangle(a,b,c)
print("area : {}".format(t.get_area()))
