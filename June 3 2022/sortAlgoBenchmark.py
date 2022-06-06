from benchmarkModule import benchmark
from customList import RandomNumbers
import random


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


    arr = [random.randrange(1, 50, 1) for i in range(30000)]
    cList = RandomNumbers()
    iterList = iter(cList)
    
    # for i in range(0,10):
    #     arr.append(next(iterList))
       # print(arr[i])

    insertionSort(arr)
    bubbleSort(arr)
    selectionSort(arr)


    numbers = list()

