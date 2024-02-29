def merge_dicts(list1):
    list2 = []
    for n in list1:
        for m in n:
            list2.append(m)

    return list2
        



d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
print(merge_dicts([d1, d2, d3]))
#print(merge_dicts([d1, d2, d3], True))
