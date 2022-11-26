from typing import List

def merge_sort(array:List[float]):
    
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(right)
        merge_sort(left)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
