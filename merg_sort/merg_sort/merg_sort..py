def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[ : mid]
        right = arr [mid :]

        # sort the left side
        Mergesort(left)

        # sort the right side
        Mergesort(right)
       
# merge the sorted left and right sides together
        return Merg(left, right, arr)

def Merg(left, right, arr):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j +=  1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j +=  1
            k += 1

        return arr

if __name__ =='__main__':
    print(Mergesort([20,18,12,8,5,-2]))
    print(Mergesort([5,12,7,5,5,7]))
    