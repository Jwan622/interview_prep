def max_sum_subarray_of_size_k(arr,k):
    max_sum = float('-inf')
    window_sum = 0
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
k = 3
print(max_sum_subarray_of_size_k(arr, k))
