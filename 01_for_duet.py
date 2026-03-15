


list_tup1 = [ (1, 2), (3, 4), (5, 6), (7, 8)]
# for item in list_tup1:
#     a = item[0]
#     b = item[1]
#     print(a, b)

for a, b in list_tup1:
    print(a, b)

list_tup1 = [ ['a', 'b'], {3, 4}, [5, 6], {7, 8}]
for a, b in list_tup1:
    print(a, b)

# list_tup1 = [ ['a', 'b'], {3, 4, 6}, [5, 6], {7, 8}]
# for a, b in list_tup1:  # ERROR!!! because {3, 4, 6}
#     print(a, b)

list_tup1 = [ ['a', 'b', 'c'], {3, 4, 5}]
for a, b, c in list_tup1:
    print(a, b, c)


d1 = {'name': 1, 'last': 2, 'id_number': 3}
for key, value in d1.items():
    print(key, value)

from pprint import pprint
pprint(d1, width = 1)