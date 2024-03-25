"""
merge intervals @ leetcode

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def create_intervals(intervals):
  intervals.sort(key=lambda x: (x[0], x[1]))

  final_intervals = []
  possible_lowest, possible_highest = intervals[0]
  for interval in intervals:
    low, high = interval

    if low <= possible_highest:
      possible_highest = high

    if low > possible_highest:
      final_intervals.append([possible_lowest, possible_highest])
      possible_lowest = low
      possible_highest = high

  final_intervals.append([possible_lowest, possible_highest])
  print('final_intervals: ', final_intervals)
  return final_intervals


intervals1 = [[1,3],[2,6],[8,10],[15,18]]
assert create_intervals(intervals1) == [[1,6],[8,10],[15,18]]


intervals2 = [[1,4],[4,5]]
assert create_intervals(intervals2) == [[1,5]]


intervals3 = [[4,5], [1,4]]
assert create_intervals(intervals3) == [[1,5]]
