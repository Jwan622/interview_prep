# cool sliding window algorithm
# we're doing most 2 - most 1 = exactly 2
# how it works:
# if the letters are pq, there are 3 distinct ways of making at most 2 substrings. If it's pqp, there are 6 ways: "p", "q", "p" (the 2nd one), "pp", "qp", "pqp". If it's "pqpq", then there are 10 ways. If there  "pqpqs", there are now 3
# keys in the char_freq so we can't make a substring with the s key until we slide the window from the left forward. That's what the while loop does until there are k keys in the char_freq again. that happens whwen right = 4 and when left = 3 which is the 2nd q.
# Then the char freq just has q and s as keys and there are 2 ways to make that which is why we add 2 to the count which is right - left + 1
def count_substrings_with_k_distinct(s, k):
    def at_most_k_distinct(characters, k):
        # This helper function counts the number of substrings with at most k distinct characters.
        count = 0
        left = 0
        char_freq = {}

        for right in range(len(characters)):
            if characters[right] not in char_freq:
                char_freq[characters[right]] = 0
            char_freq[characters[right]] += 1
            print(f'char_freq line 12: ', char_freq)
            while len(char_freq) > k:
                char_freq[characters[left]] -= 1
                print(f'char_freq line 15: ', char_freq)
                if char_freq[characters[left]] == 0:
                    del char_freq[characters[left]]
                print(f'char_freq line 18: ', char_freq)
                left += 1
            print(f'char_freq line 20: ', char_freq)
            count += right - left + 1
            print('count on line 22: ', count)
        print(f'for s, and k, count is: ', count)
        return count

    # The total number of substrings with exactly k distinct characters is the difference
    # between the number of substrings with at most k distinct characters and
    # the number of substrings with at most (k-1) distinct characters.
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)


# Example usage
s = "pqpqs"
k = 2
print(count_substrings_with_k_distinct(s, k))

