import time
import random

def benchmark(func):

    def inner(*args, **kwargs):

        start = time.time()
        value = func(*args, **kwargs)
        end  = time.time()
        runtime = end - start
        print(f"The {func.__name__} took {runtime} seconds to complete the function")

        return value

    return inner

'''@benchmark
def fibonacci(limit): 

    while a < limit:

        yield a
        a, b  = b, a+b'''

@benchmark
def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j + 1] = key 

@benchmark
def bubbleSort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + i]:
                temp  = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

@benchmark
def selectionSort(arr):

    for i in range(len(arr)):

        minIdx = i

        for j in range(i+1, len(arr)):
            if  arr[minIdx] > arr[j]:
                minIdx = j
        
        arr[i], arr[minIdx] = arr[minIdx], arr[i]


if __name__ == "__main__":

    try:
        arr = [54,76,87,45,342,23,12,34,6,7,87,5,4,3]
        
        insertionSort(arr)
        bubbleSort(arr)
        selectionSort(arr)


    except:
        pass

    '''try:
        x = fibonacci(1000000000000000000000000)
        fibList = []

        for i in x:
            fibList.append(i)
        
        for i in range(len(fibList)):
            print(fibList[i])
            
    except StopIteration as e:
        pass'''