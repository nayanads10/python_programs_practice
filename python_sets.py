"""
what is sets?
set is mutable, but items inside set is unchangeable, it is unordered, unindexed collection of item.
set is enclosed between {} . set doesnot allow duplicates
Note: Internally items of set is mapped to hash key
"""

empty_set = set()
print("the value of set is {}".format(empty_set))

set_a = {"a", 1, "b", 2}

"""
Difference between list and sets:
list: 
* list is ordered collection
* list have duplicate 
* Existing item of list can be changed
* list is slow compared to set (if we fetch an item from list it iterates through all the index)

Sets: 
* set is unordered collection
* set does not have duplicates
* Existing item of sets cannot be changed
* set is faster compared list (internally set is mapped to hash key)
"""

# add - we can add single item to set
set_a = {"a", 1 , "b", 2}
set_a.add("c")
print("the value of set after adding c is {}".format(set_a))

# update - we can add multiple items to sets
set_a.update({8,7})
print("the value of set after updating 7 and 8 is {}".format(set_a))

# remove - it throws an error if element is not present
set_b = {"a", "b", "c", "d", "e", "f", "g"}
set_b.remove("e")
print("the value after removing e is {}".format(set_b))

# discard - it returns none if element is not present
setb = set_b.discard("e")
print("the value after discarding is {}".format(setb))
set_b.discard("g")
print("the value after discarding is {}".format(set_b))

# pop - it will delete some random item in sets
set_b.pop()
print("the value of set b after pop is {}".format(set_b))

# clear - it will delete all the elements or items
set_b.clear()
print("the value of set b after clear is {}".format(set_b))

# union of sets
set_x = {1, 2, 3}
set_y = {3, 4, 5}
union_set = set_x.union(set_y)
print("the value of union of sets is {}".format(union_set))

# intersection of sets
intersection_set = set_x.intersection(set_y)
print("the value of intersection of sets is {}".format(intersection_set))

set_z = {1, 2, 3, 4, 1}
set_c = frozenset(set_z)
print("the value after freezing is {}".format(set_c))

# removing duplicates in list
lst_a = [1, 2, 1, 4, 6, 3, 8, 2]
lst_b = list(set(lst_a))
print("the value after removing duplicates is {}".format(lst_b))