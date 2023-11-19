from src.ip_leetcode import Solution
from src.my_solution import Solution as MySolution

# s = Solution()

# actual = s.restoreIpAddresses('101023')
# expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# assert len(actual) == len(expected)
# assert actual.sort() == expected.sort()

m = MySolution()
actual = m.restore_ip_address('0000')
expected = ["0.0.0.0"]
assert len(actual) == len(expected)
assert actual.sort() == expected.sort()

actual = m.restore_ip_address('101023')
expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
assert len(actual) == len(expected)
assert actual.sort() == expected.sort()

actual = m.restore_ip_address('25525511135')
print('actual ---->', actual)
expected = ["255.255.11.135", "255.255.111.35"]
assert len(actual) == len(expected)
assert actual.sort() == expected.sort()
