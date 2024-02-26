# cool sliding window algorithm
# we're doing most 2 - most 1 = exactly 2

# how it works:
# number of ways to make 2 distincts exactly = ways to make at most 2 distincts - ways to make at most 1 distinct
# first example
# if the letters are pq, there are 3 distinct ways of making at most 2 substrings ("p", "q", "pq"). The way this algo.py does this is pretty interesting though. It doesn't do the permutations of each letter.. but attempts to keep it to linear time.
# If it's pqp, there are 6 ways: "p", "q", "p" (the 2nd one), "pp", "qp", "pqp". If it's "pqpq", then there are 10 ways. If there  "pqpqs", there are now 3. remember each function call calculates the "at most" k distinct character substrings which is why when you add a letter, you get the length of the substring more counts. we eventually subtract off substring counts to get the exact k substring count. It's tricky!
# if the len of the char_freq hash ever gets > k so the number of keys is bigger, than we subtract off the left until we get = k or below. we delete left most characters from char hash until our char_length is below k because we want to increment count only when there are substrings of k or less. so we make the window smaller from the left until we get there inside the while loop.
# keys in the char_freq so we can't make a substring with the s key until we slide the window from the left forward. That's what the while loop does until there are k keys in the char_freq again. that happens whwen right = 4 and when left = 3 which is the 2nd q.
# Then the char freq just has q and p as keys and there are 2 ways to make that which is why we add 2 to the count which is right - left + 1
# some notes
# count += window_end - left + 1 that line works because with each additional letter in the window, the number of additional combinations of distincts goes up by the size of the window which is window_end - left + 1
def count_substrings_with_k_distinct(s, k):
    def at_most_k_distinct(characters, k):
        # This helper function counts the number of substrings with at most k distinct characters.
        count = 0
        left = 0
        char_freq = {}

        for window_end in range(len(characters)):
            if characters[window_end] not in char_freq:
                char_freq[characters[window_end]] = 0
            char_freq[characters[window_end]] += 1
            print(f'char_freq line 23: ', char_freq)
            while len(char_freq) > k:
                char_freq[characters[left]] -= 1
                print(f'char_freq line 26: ', char_freq)
                if char_freq[characters[left]] == 0:
                    del char_freq[characters[left]]
                print(f'char_freq line 29: ', char_freq)
                left += 1
            print(f'char_freq line 31: ', char_freq)
            count += window_end - left + 1
            print('count on line 33: ', count)
        print(f'for s, and k, count is: ', count)
        return count

    # The total number of substrings with exactly k distinct characters is the difference
    # between the number of substrings with at most k distinct characters and
    # the number of substrings with at most (k-1) distinct characters.
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)



print('onto test 1 =====================')
assert count_substrings_with_k_distinct('pq', 2) == 1, 'test 1 simple case does not pass'
print('onto test 2 ====================')
assert count_substrings_with_k_distinct('pqpq', 2) == 6, 'test 2 simple case does not pass'
print('onto test 3 =====================')
assert count_substrings_with_k_distinct('pp', 2) == 0, 'test 3 simple case does not pass'
print('onto test 4 =====================')
assert count_substrings_with_k_distinct("pqpqs", 2) == 7, 'test 4 simple case does not pass'
