s = sorted([36, 5, -12, 9, -21])
s1 = sorted([36, 5, -12, 9, -21], key=abs)
s2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print('\n', s, '\n', s1, '\n', s2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score)
print('\n', L2, '\n', L3)
