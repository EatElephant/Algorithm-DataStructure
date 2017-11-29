import sys

if len(sys.argv) <= 1:
    raise NameError("No argument is given!")
else:
    for arg in sys.argv:
        print(arg)

#Handle exception
myList = [1,2,3]
print("myList: ", myList)
index = int(input("input the index you want to print"))

try:
    print("myList[index] is：", myList[index])
except IndexError as e:
    print("IndexError happen, index out of bound " + str(e.args))
    print("the length of myList is %d, your index is %d!" % (len(myList), index))
