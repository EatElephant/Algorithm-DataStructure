import random

def quick_sort(array, start, end):
    size = end - start + 1
    if size <= 0:
        return []

    p = end

    for i in range(end - 1, start - 1, -1):
        if array[i] >= array[p]:
            array.insert(end, array.pop(i))
            p -= 1
    left = quick_sort(array, start, p-1)
    right = quick_sort(array, p+1, end)


def test():
    array1 = [random.randint(0,100) for i in range(10)]
    print("array1:  " + str(array1))
    result1 = quick_sort(array1, 0, len(array1) - 1)
    print("result1: " + str(array1))

if __name__ == "__main__":
    test()
