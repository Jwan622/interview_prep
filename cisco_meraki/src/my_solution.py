from typing import List


class Solution:
    def restore_ip_address(self, s: str) -> List[str]:
        length_of_string = len(s)
        ips_found = []
        stack = [([], 0)]

        while stack:
            ip, i = stack.pop()

            for j in range(i + 1, length_of_string + 1):
                segment = s[i:j]

                if int(segment) > 255:  # these 2 guard clauses are invalid so they need to go before the stack.append
                    break
                if j == length_of_string:   # basically if we're at the end we need to take the long segment and make smaller ones
                    if len(ip) == 3:
                        ips_found.append(ip + [segment])
                    break
                stack.append((ip + [segment], j))  # this has to go before the 0 check becauase if segment is 0, we want to add 0 as a valid ip part and then continue
                if segment == '0':
                    break

        return ['.'.join(ip) for ip in ips_found]


