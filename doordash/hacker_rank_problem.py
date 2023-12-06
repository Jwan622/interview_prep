# We want to build recommendations based on what your friends like
# friends_lst represents your friends. we're going to make recommendations to you based on restaurants they liked and what you haven't liked yet.
# visits represents restaurants you and some other customers have already visited.


def generate_referrals(visits, friends_lst):
    recs = {}

    for couple in friends_lst:
        friend = couple[1]
        me = couple[0]
        if friend not in visits.keys():
            continue
        for rest in visits[friend]:
            print('rest: ', rest)
            print('me: ', me)
            if me not in visits.keys() or rest not in visits[me]:
                if me in recs:
                    recs[me] += [rest]
                else:
                    recs[me] = [rest]

    print('recss: ', recs)
    return recs


print('test case 1 started')
visits = {1: ['apple bees', 'bjs'], 2: ['chilis', 'mcdonalds'], 10: ['starbucks']}
friends_lst = [[1,2]]
expected = {1: ['chilis', 'mcdonalds']}
assert sorted(generate_referrals(visits, friends_lst).keys()) == sorted(expected.keys())
assert len(expected) == len(generate_referrals(visits, friends_lst))
for k in expected:
    assert sorted(generate_referrals(visits, friends_lst)[k]) == sorted(expected[k])
print('test case 1 passed')


print('test case 2 started')
visits = {1: ['apple bees', 'bjs'], 2: ['chilis', 'mcdonalds'], 10: ['starbucks']}
friends_lst = [[8,9]]
expected = {}
assert sorted(generate_referrals(visits, friends_lst).keys()) == sorted(expected.keys())
assert len(expected) == len(generate_referrals(visits, friends_lst))
for k in expected:
    assert sorted(generate_referrals(visits, friends_lst)[k]) == sorted(expected[k])
print('test case 2 passed')


print('test case 3 started')
visits = {1: ['apple bees', 'bjs'], 2: ['apple bees', 'mcdonalds'], 10: ['starbucks']}
friends_lst = [[1,2], [3,1]]
expected = {1: ['mcdonalds'], 3: ['apple bees', 'bjs']}
assert sorted(generate_referrals(visits, friends_lst).keys()) == sorted(expected.keys())
assert len(expected) == len(generate_referrals(visits, friends_lst))
for k in expected:
    assert sorted(generate_referrals(visits, friends_lst)[k]) == sorted(expected[k])
print('test case 3 passed')
print('ALL TESTS PASS')


print('playing around with some list methods')
list1 = [1,2,3]
nested_list1 = [[1,2], [1,3], [2,3], [3,4]]

reverse_list1 = list1[::-1]
print('reversed list: ', reverse_list1)

flattened_list_comp_1 = [ele for couple in nested_list1 for ele in couple]
print('flattened list comp: ', flattened_list_comp_1)

appended_nested_list1 = [[couple, couple[::-1]] for couple in nested_list1]
print('appended_nested_list1: ', appended_nested_list1)





