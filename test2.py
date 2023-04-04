list1 = [1, 2, 3, 4, 9]
list2 = [1, 2, 3, 4, 5]
print(set(list2) - set(list1))
print(set(list1) - set(list2))

aa = [{"a": "1", "b": "2"}, {"a": "3", "d": "4"}]
a2 = [i['a'] for i in aa]
print(a2)
