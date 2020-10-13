# Array
def printarray(arrays):
    print("this array members is now : ")
    print(arrays)
    for i in range(len(arrays)):
        print("index[{}] : ".format(i), end="")
        print(arrays[i])
    print()


a = [1, 2, 3]
b = [9, 12, 35, 4]
printarray(a)
a.append(4)
print("append 4 ")
printarray(a)
a.pop(1)
print('remove index 1')
printarray(a)
b.sort()
print("sorted b array")
printarray(b)
b.sort(reverse=-1)
print("reverse sorted array b")
printarray(b)
a.extend(b)
print("exteneded a with b")
printarray(a)
a.insert(1, 2)
print("inserting (2) in index(1) in a array")
printarray(a)
a.sort()
print("sorted a")
printarray(a)
a.remove(4)
print("remove first 4 in a array")
printarray(a)
x = a.index(4)
print("showing value on 4 index")
print(x)
a.extend(b)
a.append(4)
printarray(a)
c = 4
x = a.count(c)
print("there are {},(({})) in this array".format(x, c))
d = a.copy()
printarray(d)
a.clear()
print("cleared a array")
printarray(a)
e = slice(0, len(d), 2)
print("slieced d array with step 2 ")
print(d[e])

# search in arrays
# lieaner search

# define Binary search


def binarySearch(arr, low, high, x, com_act):
    com_act += 1
    if high >= low:
        mid = int((low+high)/2)
        if arr[mid] == x:
            return mid, com_act
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x, com_act)
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, high, x, com_act)
    elif low > high:
        return binarySearch(arr, high, low, x, com_act)


select = int(
    input("please Select type of search (1)->linear  &&  (2)->(binary)"))
x = int(input("Enter a integer Number : "))
if select == 1:
    for i in range(len(d)):
        if d[i] == x:
            print("{} is in the array with index of {}".format(x, i))
            print("we have find your input with {} Comparison action".format(i+1))
            break
    else:
        print("Not Found,Number of Comparsion action{}".format(len(d)+1))
elif select == 2:
    num, com = binarySearch(d, 0, len(d)-1, x, 0)
    print("{} is in the array with index of {}".format(x, num))
    print("we have find your input with {} Comparison action".format(com))

else:
    print("Worng Selecting Number")
# binary Search
