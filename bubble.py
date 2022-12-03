from typing import List, Any

def bubble_sort(array: List[Any]) -> int:
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j][1] > array[j+1][1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                movements += 1
