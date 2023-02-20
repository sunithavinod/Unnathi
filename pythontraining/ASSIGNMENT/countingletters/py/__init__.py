
sentence1 =" Sunsunday"
count = {}
for i in sentence1:
    if i in count:
        count[i.lower()] = count[i.lower()] + 1
    else:
        count[i.lower()] = 1
print(count['s'])




# program to find length of string
def Len(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


str = "unnathi"
print(Len(str))
