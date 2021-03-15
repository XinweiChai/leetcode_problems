import heapq


def heap_sort(a):
    heapq.heapify(a)
    return heapq.nsmallest(len(a), a)


print(heap_sort([7, 1, 6, 5, 3, 2, 4]))
