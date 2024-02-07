def max_sum_subarray_of_size_k(arr, k):
    window_sum = 0
    max_sum = 0
    window_start = 0

    # Slide window across array
    for window_end in range(len(arr)):
        print('window_end: ', window_end)
        print('arr[window_end]: ', arr[window_end])
        window_sum += arr[window_end] # Add the next element into the window sum
        print('window_sum: ', window_sum)
        if window_end >= k - 1: #remember that window_end is an index so if k is 3 this means the window is too big now
            max_sum = max(max_sum, window_sum)
            print('max_sum: ', max_sum)
            window_sum -= arr[window_start] # we already recorded max sum so lets make the window smaller and decrease the sum by the beginning of the window so we can add on the next run
            print('window_sum after we subtract the front element: ', window_sum)
            window_start += 1

    return max_sum


arr = [1,3,-1,-3,5,3,6,7]
assert max_sum_subarray_of_size_k(arr, 3) == 16, 'test 1 does not equal 16 even though it should'

arr = [1,2, 3, 4]
assert max_sum_subarray_of_size_k(arr, 3) == 9, 'test 2 does not equal 9 even though it should'

arr = [4, 3, 2, 1]
assert max_sum_subarray_of_size_k(arr, 3) == 9, 'test 3 does not equal 9 even though it should'

arr = [0, 0, 0, 1]
assert max_sum_subarray_of_size_k(arr, 3) == 1, 'test 2 does not equal 1 even though it should'
