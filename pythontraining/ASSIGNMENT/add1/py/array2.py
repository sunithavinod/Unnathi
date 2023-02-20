arr_str = ['P'] * 5
print(arr_str)

##
arr = []
arr = [0 for i in range(5)] 
print(arr)

##
arr_str = ['P'] * 5
print(arr_str)


##
class Employee:
    id=10
    name="Harish"
    def display(self):
        print(self.id,self.name)


##
import array as arr

numbers = arr.array('i', [10, 11, 12, 12, 13])

(numbers.remove(12))
print(numbers)   # Output: array('i', [10, 11, 12, 13])

print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])
