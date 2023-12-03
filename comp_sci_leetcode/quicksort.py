# Here's a simple version of Quicksort with recursion
# the algo works by finding a pivot (any random number but here we use the high index
# we move all elements smaller than the pivot to the left
# we move all elements bigger than the pivot to the right
def quicksort(arr):
    print('arr: ', arr)
    # Base case: arrays with less than 2 elements are already sorted
    if len(arr) == 1 or len(arr) == 0:
        return arr

    # Choosing the first element as the pivot
    pivot = arr[0] # pivot can be anything, let's pick the first element
    print('pivot: ', pivot)

    # Separating elements smaller and larger than the pivot
    smaller = [i for i in arr[1:] if i <= pivot] # we use index 1 since we use the 0 index element as the pivot
    print('smaller: ', smaller)
    larger = [i for i in arr[1:] if i > pivot]
    print('larger: ', larger)

    # Recursive calls and concatenating results
    return quicksort(smaller) + [pivot] + quicksort(larger)


# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Sorted array:", quicksort(arr))

# recursive tree looks like this:
#  [3, 6, 8, 10, 1, 2, 1]
# Left: [1,2,1]
# Left: [1]
# right: [2]
# right: [6,8,10]
# left: []
# right: [8,10]
# left: []
# right: [10]
# done

# here's a version with recursion that doesn't use the middle trick and sorts it in place of the original array

# def quicksort(arr, low, high):
#     if low < high:
#         # Partition the array
#         pi = partition(arr, low, high)
#         print('pi: ', pi)
#
#         # Recursively sort the sub-arrays
#         quicksort(arr, low, pi - 1)  # Before pi
#         quicksort(arr, pi + 1, high)  # After pi
#
#
# def partition(arr, low, high):
#     print('arr: ', arr)
#     # Pivot (Element to be placed at right position)
#     pivot = arr[high]
#     print('pivot: ', pivot)
#     i = low - 1  # i is eventually used to figure out where to place pivot. we decrement because if we find an element smaller than pivot, we want to move i up 1
#     print('i as  low - 1: ', i)
#     for j in range(low, high):
#         print('j: ', j)
#         # If current element is smaller than or equal to pivot, swap i + 1 and j
#         if arr[j] <= pivot:
#             i = i + 1   # we put it at i + 1 so the smaller element arr[j] will be put at the left
#             print('i as i + 1: ', i)
#             arr[i], arr[j] = arr[j], arr[i]
#     print('arr before swap: ', arr)
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]  # put the pivot at i + 1 since all the elements smaller than pivot were put at i + 1. we increment i again to ensure all the small elements are put at the pivot's left.
#     print('pivot: ', pivot)
#     print('arr after swap, partition should be correctly placed...everything bigger than pivot is to the right', arr)
#     return i + 1
#
#
# # Example usage
# arr = [10, 7, 8, 9, 1, 5]
# quicksort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)

# while swapping, if the array looks like [1, 5, 8, 9, 10, 7] and the pivot is 7, and if i starts at 1, we find that all the elements from low to high are greater than pivot, then we place the pivot at i + 1 which will ensure that all the greater elements are now to the right of the pivot and the new array looks like [1,5,7,8,9,10].
