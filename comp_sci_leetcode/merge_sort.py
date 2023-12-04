"""
I believe that the key to understanding merge sort is understanding the following principle -- I'll call it the merge principle:

Given two separate lists A and B ordered from least to greatest, construct a list C by repeatedly comparing the least value of A to the least value of B, removing the lesser value, and appending it onto C. When one list is exhausted, append the remaining items in the other list onto C in order. The list C is then also a sorted list.
"""


# def merge(arr, left_index, mid_index, right_index):
#     n1 = mid_index - left_index + 1
#     n2 = right_index - mid_index
#
#     print('n1: ', n1)
#     print('n2: ', n2)
#
#     # create temp arrays
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # Copy data to temp arrays L[] and R[]
#     for i in range(0, n1):
#         print('i in range 0 to n1', i, n1)
#         L[i] = arr[left_index + i]
#
#     for j in range(0, n2):
#         print('j in range 0 to n2', j, n2)
#         R[j] = arr[mid_index + 1 + j] # this gets a different element than before
#
#     # Merge the temp arrays back into arr[l..r]
#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = left_index  # Initial index of merged subarray
#     print('L: ', L)
#     print('R: ', R)
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#
# # l is for left index and r is right index of the
# # sub-array of arr to be sorted
#
#
# def mergeSort(arr, left_most_index, right_most_index):
#     if left_most_index < right_most_index:
#         # Same as (l+r)//2, but avoids overflow for
#         # large l and h
#         mid = left_most_index + (right_most_index - left_most_index) // 2
#         print('arr: ', arr)
#         print('left most index: ', left_most_index)
#         print('right most index: ', right_most_index)
#         print('mid index: ', mid)
#
#         # Sort first and second halves
#         print('calling first MergeSort', arr)
#         mergeSort(arr, left_most_index, mid) # this stops once left == mid which becomes the right most index
#         print('calling second MergeSort', arr)
#         mergeSort(arr, mid + 1, right_most_index)
#         print('calling merge now', arr)
#         merge(arr, left_most_index, mid, right_most_index)
#
#
# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is: ")
# for i in range(n):
#     print("%d" % arr[i], end=" ")
#
# mergeSort(arr, 0, n - 1)
#
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i], end=" ")


def merge_sort(list): # this is the divide part (divide and conquer)
    print('list in merge sort: ', list)
    if len(list) <= 1:  # this allows us to return a single value for left and right below. once we sort something like 16,9 as 9,16, then we bubble up. then we can sort left, and then 9,16
        return list  # base case that keeps up from recursioning

    middle = len(list) // 2
    print('middle: ', middle)
    left = merge_sort(list[:middle])  # we sort this all the way before moving to right
    right = merge_sort(list[middle:]) # at some point you'll see left [14], right [9,16] and that's because we bubble up one recursion level.
    print('left: ', left)
    print('right: ', right)

    return merge(left, right)


def merge(left, right):  # this is the sort/conquer part
    result = []
    pointer_for_left = 0
    pointer_for_right = 0
    print('left in merge: ', left)
    print('right in merge: ', right)
    while pointer_for_left < len(left) and pointer_for_right < len(right): # basically we have a left and a right and we compare the lists and add the lesser to a new list and return that new list
        if left[pointer_for_left] <= right[pointer_for_right]:
            result.append(left[pointer_for_left])
            pointer_for_left += 1
        else:
            result.append(right[pointer_for_right])
            pointer_for_right += 1

    print('intermediate result: ', result)
    print('pointer_for_left now: ', pointer_for_left)
    print('pointer_for_right now: ', pointer_for_right)
    print('whats to append on left: ', left[pointer_for_left:])
    print('whats to append on right: ', right[pointer_for_right:])
    result += left[pointer_for_left:]
    result += right[pointer_for_right:]  # we can do this because the lists are already sorted so the remainder has to be greater than what's in result
    print('result: ', result)
    return result


thing = [12,11,14,9,16]
print(merge_sort(thing))


"""
It looks like this:
                        [12,11,14,9,16]
                    |                  |               
                    |                  |
                [12,11]             [14,9,16]
             |           |        |              |
             |           |        |              |
         [12]--conquer---[11]    [14]--conquer-- [9,16]
                                                |         | 
                                               [9]--conquer--[16]         
             
"""
