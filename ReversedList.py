def reversed_List(lst1, lst2):
    compare_to = []
    for item in range(len(lst1)):
        compare_to.append(lst1.pop())
    if compare_to == lst2:
        return True
    else:
        return False

print (reversed_List([1, 2, 3], [3,2,1]))
print (reversed_List([1, 5, 3], [3,2,1]))