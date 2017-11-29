import random

def bubble_sort(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

def sel_sort(array):
    length = len(array)

    for i in range(length-1):
        min_index = i
        for j in range(i, length):
            if array[min_index] > array[j]:
                min_index = j
        min_value = array[min_index]
        array[min_index] = array[i]
        array[i] = min_value

    return array

def insert_sort(array):
    length = len(array)

    for i in range(1,length):
        x = array[i]
        for j in range(i-1, -1, -1):
            if array[j] >= x:
                array[j+1] = array[j]
                if j == 0:
                    array[j] = x
            else:
                array[j+1] = x
                break

    return array

def merge_sort(array):
    # print(array)
    if len(array) <= 1:
        return array
    else:
        mid = int(len(array)/2)
        left = merge_sort(array[0:mid])
        right = merge_sort(array[mid:])
        result = []
        while len(left) != 0 or len(right) != 0:
            if not len(left):
                result.append(right.pop(0))
            elif not len(right):
                result.append(left.pop(0))
            else:
                if left[0] > right[0]:
                    result.append(right.pop(0))
                else:
                    result.append(left.pop(0))
        return result

def quick_sort(array):
    length = len(array)
    if length > 1:
        p = length - 1          #last element is choose as pivot
        for i in range(length-2, -1, -1):
            if array[i] > array[p]:
                array.append(array.pop(i))
                p -= 1
        array[0:p] = quick_sort(array[0:p])
        array[p+1:] = quick_sort(array[p+1:])
    return array

def quick_sort2(array, start, end):
    if end <= start:
        return

    p = end
    for i in range(end - 1, start - 1, -1):
        if array[p] < array[i]:
            array.insert(p, array.pop(i))
            p -= 1

    quick_sort2(array, start, p-1)
    quick_sort2(array, p+1, end)


def createTestData(n):
    res = []
    for i in range(n):
        res.append(int(100 * random.random()))
    print("test data: " + str(res))
    return res

def test():
    print("Below are sorting algorithm with complexity of O(n^2)\n")
    test1 = createTestData(10)
    print("result of bubble_sort: " + str(bubble_sort(test1)))
    test2 = createTestData(10)
    print("result of selection_sort: " + str(sel_sort(test2)))
    test3 = createTestData(10)
    print("result of insert_sort:" + str(insert_sort(test3)))
    print("Below are sorting algorithm with complexity of O(nlog(n))\n")
    test4 = createTestData(10)
    print("result of merge_sort:" + str(merge_sort(test4)))
    test5 = createTestData(10)
    print("result of quick_sort:" + str(quick_sort(test5)))
    test6 = createTestData(10)
    quick_sort2(test6, 0, len(test6)-1)
    print("result of quick_sort2:" + str(test6))




if __name__ == "__main__":
    test()
