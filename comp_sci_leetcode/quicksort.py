# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    print('low: ', low)
    print('high: ', high)
    pivot = array[high]
    print('pivot ', pivot)
    # pointer for greater element
    i = low - 1
    print('i: ', i)

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        print('j: ', j)
        if array[j] <= pivot:
            print('insdie swap', array[j])
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            print('increment i: ', i)
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    print('array: ', array)
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print('array after swap: ', array)
    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        print('pi', pi)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
