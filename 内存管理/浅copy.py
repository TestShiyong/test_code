import copy

li = [1, 2, 3]

list1 = [4, 5, 6, li]

list2 = list1

list3 = list1.copy()

list4 = copy.deepcopy(list1)


print(id(li),li)
print(id(list1),list1,'lsit1')
print(id(list2),list2,'lsit2')
print(id(list3),list3,'lsit3')
print(id(list3),list3,'lsit4')
list1.append('aa')
li.append('cc')

print(id(list1),list1,'lsit1')
print(id(list2),list2,'lsit2')
print(id(list3),list3,'lsit3')
print(id(list4),list4,'lsit4')
