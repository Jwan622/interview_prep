# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'paperCuttings' function below.
# This was the runner they used for the test but I don't have to use it here.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER textLength
#  2. INTEGER_ARRAY starting
#  3. INTEGER_ARRAY ending
#
from multiprocessing import Pool


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     textLength = int(input().strip())
#
#     starting_count = int(input().strip())
#
#     starting = []
#
#     for _ in range(starting_count):
#         print('starting count: ', starting_count)
#         starting_item = int(input().strip())
#         print('starting_item: ', starting_item)
#         starting.append(starting_item)
#
#     ending_count = int(input().strip())
#
#     ending = []
#
#     for _ in range(ending_count):
#         print('ending coiunt: ', ending_count)
#         ending_item = int(input().strip())
#         print('ending item: ', ending_item)
#         ending.append(ending_item)
#
#     result = paperCuttings(textLength, starting, ending)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


def check_non_overlapping(pair):
    seg1, seg2 = pair
    return seg1[1] < seg2[0]


def paper_cuttings(text_length, starting, ending):
    # Zip starting and ending together and sort the pairs
    segments = sorted(zip(starting, ending))

    # Remove duplicates
    segments = list(dict.fromkeys(segments))
    print('segments: ', segments)
    # Create a pool of worker processes
    with Pool() as pool:
        # Generate all possible pairs of segments
        pairs = ((segments[i], segments[j]) for i in range(len(segments)) for j in range(i + 1, len(segments)))

        # Use parallel processing with imap to check non-overlapping pairs
        # Set the chunksize as per your requirement
        non_overlapping_pairs = pool.imap_unordered(check_non_overlapping, pairs, chunksize=10)
        print('non overlapping pairs: ', non_overlapping_pairs)
        # Count non-overlapping pairs
        count = sum(non_overlapping_pairs)
        print('count', count)

    return count

"""
In this modification:

chunksize is a parameter you can adjust depending on your dataset size and available resources. It determines how many tasks are sent to each worker process at a time.

pool.imap is similar to pool.map, but it returns an iterator instead of a list. This can be more memory efficient for large datasets.
If the order of results is not important, use pool.imap_unordered, as it can be faster.

Remember, tuning the chunk size depends on the nature of the task and the system's resources. A larger chunk size can reduce overhead by sending fewer, larger batches of tasks to worker processes, but it may lead to unequal workload distribution among the processes. Experimenting with different chunk sizes can help find the optimal setting for your specific case.

my concern was that the pairs list wwas too big, so we changed it to a generator:

If the pairs list is too large to fit into memory, using a generator is a good approach to handle this memory issue. Generators allow you to iterate over data without the need to load everything into memory at once. However, there are some considerations to keep in mind when using generators with multiprocessing in Python.

When you use a generator with Pool.map or Pool.imap, the generator is consumed in the main process to create chunks of data that are then sent to the worker processes. This means that the generator's advantage of low memory usage is partially lost, as chunks of data are still created and held in memory. The size of these chunks is controlled by the chunksize parameter in imap.

Looking at the documentation for Pool.map it seems you're almost correct: the chunksize parameter will cause the iterable to be split into pieces of approximately that size, and each piece is submitted as a separate task.

So in your example, yes, map will take the first 10 (approximately), submit it as a task for a single processor... then the next 10 will be submitted as another task, and so on. Note that it doesn't mean that this will make the processors alternate every 10 files, it's quite possible that processor #1 ends up getting 1-10 AND 11-20, and processor #2 gets 21-30 and 31-40.
"""


# this fails when starting count is 100000 so we might need to use batches and multiprocess parallelism
# Test the function
if __name__ == '__main__':
    textLength = 10
    starting = [3, 1, 2, 8, 8]
    ending = [5, 3, 7, 10, 10]

    assert paper_cuttings(textLength, starting, ending) == 3, f"this does not equal 3:  {paper_cuttings(textLength, starting, ending)}"

    print('ALL TESTS PASS')
