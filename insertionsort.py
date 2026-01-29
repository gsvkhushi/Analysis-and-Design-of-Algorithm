import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    insertion_sort(l)
    e_t = time.time()
    sort_time.append(e_t - s_t)
plt.plot(n_list, sort_time, marker='x') 
plt.xlabel("Number of elements(n)")
plt.ylabel("Time taken in seconds)")
plt.title("Insertion Sort sort: Time Complexity Analysis")
plt.grid(True)
plt.savefig("insertion_sort.time_complexity.png", dpi=300,bbox_inches='tight')
plt.show()

print("Input sizes:", n_list)
print("Sorting times:", sort_time)
