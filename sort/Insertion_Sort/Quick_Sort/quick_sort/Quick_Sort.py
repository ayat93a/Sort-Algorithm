def partition(array, min, max):
    pivot = array[max]
    i = min - 1
    for j in range(min, max):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[max]) = (array[max], array[i + 1])
# return the position from where the partition is done
    return i + 1


def QuickSort(array, min, max):
    if min < max:
        sub_array = partition(array, min, max)
        QuickSort(array, min, sub_array - 1)
        QuickSort(array, sub_array + 1, max)
    return

if __name__ == '__main__':
    print (QuickSort([5,9,12,55,90] , 1,2))