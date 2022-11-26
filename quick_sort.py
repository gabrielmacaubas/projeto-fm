def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high][1] >= pivot[1]:
            high = high - 1

        while low <= high and array[low][1] <= pivot[1]:
            low = low + 1
            
        if low <= high:
            array[low], array[high] = array[high], array[low]

        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    