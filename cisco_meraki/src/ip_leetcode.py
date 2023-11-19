from typing import List

class Solution:
    # we have to backtrack and attempt other possibilities. subnodes on the way. lends well to a graph. Let's try a depth-first approach to solving this
    def restoreIpAddresses(self, s: str) -> List[str]:
        length_of_string, stack, ips_found = len(s), [([], 0)], []
        print('length_of_string: ', length_of_string)
        print('stack: ', stack)  # we store the index too because we use it to look ahead
        print('ips_found: ', ips_found)  # this is used to store valid ips
        while stack:  # depth first search. we initialize it with the starting index and an empty ip list. we create an ip and then backtrack to prior valid ips.
            ip, i = stack.pop()  # we have a tuple to keep track of the ip and the index
            print('ip popped: ', ip)  # pop off the number that was previously the longest it could be without going over 255 and work with that
            print('i: ', i)  # we store the index of the last valid ip so we look ahead and build from there

            for j in range(i + 1, length_of_string + 1):
                print('j: ', j)
                segment = s[i:j]  # we use i and j to build a segment of the IP
                print('segment: ', segment)
                if int(segment) > 255:
                    print('segment too large and > 255, let us pop off the last valid ip beginning and work with that')
                    break
                if j == length_of_string:  ## reach the end
                    if len(ip) == 3:
                        ips_found.append(ip + [segment])
                        print('last ip: ', ips_found)
                    break  # if reach the last index, sometimes we need to discard the segment because we only have 3 ips and we need a 4th so we throw out the segment, and try to create a shorter segment
                print('ip + segment, j: ', (ip + [segment], j))
                stack.append((ip + [segment], j)) # this builds the depth-first list to traverse, all valid ip beginnings are added to traverse later on.
                print('stack ---->: ', stack)
                if segment == '0': ## e.g. segment '01' is not valid so we pop off the 0 because it stands alone
                    print('segment is 0 so popping')
                    break
        return ['.'.join(ip) for ip in ips_found]
