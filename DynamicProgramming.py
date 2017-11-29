import random

# Maximum sum of sub array
def max_subarray(array):
    if len(array) <= 0:
        raise NameError('input empty')

    max_table = [array[0]] * len(array)
    end_max_array = array[0]
    for i in range(1, len(array)):
        if end_max_array > 0:
            end_max_array += array[i]
        else:
            end_max_array = array[i]
        max_table[i] = max(max_table[i-1], end_max_array)


    return max_table[-1]

#Bag Problem
def max_bag(c, v, limit):
    if len(c) == 0 or len(v) == 0:
        return 0
    max_value = [[0 for i in range(limit + 1)] for j in range(len(c))]
    for l in range(0,limit + 1):
        if c[0] > l:
            max_value[0][l] = 0
        else:
            max_value[0][l] = v[0]

    for i in range(1,len(c)):
        for l in range(0, limit + 1):
            if c[i] > l:
                max_value[i][l] = max_value[i-1][l]
            else:
                max_value[i][l] = max(max_value[i-1][l], max_value[i-1][l - c[i]] + v[i])

    return max_value[-1][-1]

#Fibonaci
complexity = 0
memo = [None for i in range(0,100)]
def get_fib(n):
    global complexity,memo
    complexity = 0
    fib_num = fib(n,memo)
    print("fib(%d) = %d, complexity = %d" % (n, fib_num, complexity))


def fib(n, memo):
    global complexity
    complexity += 1
    if memo[n] == None:
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]





def test():
    array1 = [1, -2, 3, 5, -3, 2]
    array2 = [0, -2, 3, 5, -1, 2]
    array3 = [-9, -2, -3, -5, -6]
    print("array1: " + str(array1) + ", max subarray sum is " + str(max_subarray(array1)))
    print("array2: " + str(array2) + ", max subarray sum is " + str(max_subarray(array2)))
    print("array3: " + str(array3) + ", max subarray sum is " + str(max_subarray(array3)))

    c = [3,5,2,7,4]
    v = [2,4,1,6,5]
    limit = 10
    print("max value can put in the bag with limit " + str(limit) + " is: " + str(max_bag(c,v,limit)))

    print("Get Fibonacci Sequence:")
    get_fib(20)
    get_fib(30)

if __name__ == "__main__":
    test()
