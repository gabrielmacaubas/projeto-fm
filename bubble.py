def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        for i in range(i):
            if array[i][1] > array[i+1][1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
