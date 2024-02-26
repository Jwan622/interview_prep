def AppendList(value, lst=[]):
	lst.insert(0, value)
	print(lst)


# lst refers to a mutable object so that changes
AppendList('x', [1,2,3])
AppendList('x')
AppendList('a') # weird right? it's because I think python doesn't garbage collect lst and keeps it in memory.
