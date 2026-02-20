import time
import matplotlib.pyplot as plt
import random

def max_heapify(arr,n,i):
    largest = i
    left = 2* i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest] :
        largest = left
    if right < n and arr[right] > arr[largest] :
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,n,largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,n,i)

def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        max_heapify(arr,i,0)
    return arr

if __name__ == "__main__":
    sizes = [5000, 6000, 7000, 8000, 9000, 10000]
    times = []
    for s in sizes:
        arr = [random.randint(1, 10000) for _ in range(s)]
        start = time.time()
        heapsort(arr)
        end = time.time()
        times.append(end - start)
    print(sizes)
    print(times)
    plt.plot(sizes, times)
    plt.show()
