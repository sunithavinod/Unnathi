     
class emp:
  def hello_emp(self,e_name=None):
   if e_name is not None:
       print("Hello",e_name)
   else:
      print("hello")
Emp1=emp()
Emp1.hello_emp()
Emp1.hello_emp("sunitha")


