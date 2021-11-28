import heapq


def heap_sort(a):
    heapq.heapify(a)
    return heapq.nsmallest(len(a), a)


def helper(arr, size, k):
    largest = k
    left = 2 * k + 1
    right = 2 * k + 2
    if left < size and arr[largest] > arr[left]:
        largest = left
    if right < size and arr[largest] > arr[right]:
        largest = right
    arr[largest], arr[k] = arr[k], arr[largest]


# O(n)
def heapify(arr):
    for i in range(len(arr) - 1, -1, -1):
        helper(arr, len(arr), i)
    return arr


if __name__ == '__main__':
    # print(heap_sort([7, 1, 6, 5, 3, 2, 4]))
    print(heapify([3, 9, 2, 1, 4, 5]))
