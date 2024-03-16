
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def uniqueify(acc, lst1_ele):
    print('acc: ', acc)
    print('lst1_ele: ', lst1_ele)
    if lst1_ele in lst2 and lst1_ele not in acc:
        acc.append(lst1_ele)
    return acc

intersection = reduce(uniqueify, lst1, [])
print(intersection)


# or
print(list(set(lst1) & set(lst2)))
