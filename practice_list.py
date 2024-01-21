
"""
what is list?
list is a group of elements which can be alphabet,numeric or alpha numeric (or) combination of all 3
list is mutable
list is enclosed between []

Note:list is mutable since it creates extra memory space it is defined
"""

lst_a = ["a","b",1,3]
emp_lst = []                                # one kind of defining empty list
print("one kind of defining empty list is {}".format(emp_lst))
emp_lst = list ()                         # another kind of defining empty list
print("another kind of defining empty list is {}".format(emp_lst))

# to find length of list
lst_x = ["a","b","c",1,2]
len_lstx = len(lst_x)
print("length of list x is {}".format(len_lstx))

# to find type
typ_lst_x = type(lst_x)
print("the type of the variable is {}".format(type(lst_x)))

lst_y = ["1","2","python",123,"@abc"]
len_lsty = len(lst_y)
print("the length of list is {}".format(len_lsty))

# indexing of lst_y
ind_lsty = lst_y[0]
print("the zeroeth index of lst_y is {}".format(ind_lsty))
ind_lsty = lst_y[1]
print("the first index of lst_y is {}".format(ind_lsty))
ind_lsty = lst_y[2]
print("the second index of list_y is {}".format(ind_lsty))
ind_lsty = lst_y[3]
print("the third index of list_y is {}".format(ind_lsty))
ind_lsty = lst_y[4]
print("the fourth index of list_y is {}".format(ind_lsty))

# to print h from python which is an item of lst_y
lst_python = lst_y[2]
print("the value is {}".format(lst_python))
lsty_h = lst_python[3]
print("the value is {}".format(lsty_h))
lst_y_h = lst_y[2][3]
print("another way of indexing {}".format(lst_y_h))
lst_y[3] = 456
print("the lst_y after changing the value is {}".format(lst_y))

"""
append: * we can add only 1 element at a time using append command
        * append is faster since its adds only one element and there is no internal iterations performed
        * time complexity is less
"""
# append - we can add only  single item
lst_y.append(123)
print("the value of lst_y after appending is {}".format(lst_y))

"""
extend: * we can add n number of elements at a time using extend command
        * extend is slow compared to append since it is iterates through out the elements it needs to be added
        * time complexity is more
"""
# extend - we can add multiple items at a time
lst_y.extend(["a","b"])
print("the lst_y after extending is {}".format(lst_y))
lst_y.extend([["3","4"]])
print("the lst_y after extending is {}".format(lst_y))



lst_c = ["#abc",789,"box","1","9"]
len_lstc = len(lst_c)
print("the length of list is {}".format(len_lstc))

# indexing of lst_c
ind_lstc = lst_c[0]
print("the zeroeth index of lst_c is {}".format(ind_lstc))
ind_lstc = lst_c[1]
print("the first index of lst_c is {}".format(ind_lstc))
ind_lstc = lst_c[2]
print("the second index of lst_c is {}".format(ind_lstc))
ind_lstc = lst_c[3]
print("the third index of lst_c is {}".format(ind_lstc))
ind_lstc = lst_c[4]
print("the fourth index of lst_c is {}".format(ind_lstc))

lst_c = ["#abc",789,"box","1","9"]
# to print x from box which as item of lst_c
lst_box = lst_c[2]
print("the value is {}".format(lst_box))
lstc_x = lst_box[2]
print("the value is {}".format(lstc_x))
lst_c_x = lst_c[2][2]
print("another way of indexing {}".format(lst_c_x))

lst_c[3] = 5
print("the lst_c after changing the value is {}".format(lst_c))

lst_c.append(123)
print("the value of lst_c after appending is {}".format(lst_c))

lst_c.extend(["a","b"])
print("the value of lst_c after extend is {}".format(lst_c))
lst_c.extend([["1","2"]])
print("the value of lst_c after extend is {}".format(lst_c))


# slicing
lst_d = ["#abc",789,"box","1","9"]
ind0_to_ind4 = lst_d[0:4]
print("the value of list from zero to fourth index is {}".format(ind0_to_ind4))
ind1_to_ind3 = lst_d[1:3]
print("the value of list from first to third index is {}".format(ind1_to_ind3))

# slicing with step size
lst_d = ["#abc",789,"box","1","9","4","3"]
len_lstd = len(lst_d)
print(len_lstd)
slc_with_stp2 = lst_d[0:7:2]
print("the value of list lst d with step size 2 is {}".format(slc_with_stp2))
slc_with_stp4 = lst_d[0:7:4]
print("the value of list lst d with step 4 is {}".format(slc_with_stp4))
slc_with_stp3 = lst_d[0:7:3]
print("the value of list lst d with step 3 is {}".format(slc_with_stp3))

lst_a = ["1","2","3","a"]
lst_a.append(4)
print("the value of lst_a after appending is {}".format(lst_a))

# item reversing in list
str_a = "welcome class"                  # output: "emoclew sslac"
str_a_lst = str_a.split(" ")
print("the list after splitting the string is {}".format(str_a_lst))

lst_ind0 = str_a_lst[0]
print(lst_ind0)
lst_ind1 = str_a_lst[1]
print(lst_ind1)

rev_ind0 = lst_ind0[::-1]
print(rev_ind0)
rev_ind1 = lst_ind1[::-1]
print(rev_ind1)

str_a_lst[0] = rev_ind0
print(str_a_lst)
str_a_lst[0] = str_a_lst[0][::-1]
print(str_a_lst)
str_a_lst[1] = str_a_lst[1][::-1]
print(str_a_lst)

str_a_rev = " ".join(str_a_lst)
print("the value after reversing items is {}".format(str_a_rev))

lst_x = [1,2,["a","b","python"],3,4]
lst_x[2][2] = lst_x[2][2][::-1]
print(lst_x)

#assignment
lst_z = ["a","b",["john","class","alex"],4,5,7]
lst_z[2][1] = lst_z[2][1][::-1]
print(lst_z)

# deleting methods
#clear - it clears all the elements in the list
lst_a = [1,2,3]
lst_a.clear()
print("list after clearing is {}".format(lst_a))

#pop - it delets last index value
lstb = ["a","b","c","d"]
lstb.pop()
print("the list after pop is {}".format(lstb))
lstb.pop()
print("the list after pop is {}".format(lstb))
lstb.pop()
print("the list after pop is {}".format(lstb))

# remove - we can specify which item or element to be deleted from list
lstc = ["john","bob","alex","xyz"]
lstc.remove("bob")
print("the value after removing bob from list is {}".format(lstc))
lstc.remove("john")
print("the value after removing john from list is {}".format(lstc))

# reverse
lstd = [1, 2, 3, 4]
lstd.reverse()
print("The list after reversing is {}".format(lstd))

# insert and index
lstx = ["a", "b", "c", "d", "e"]
ind_val = lstx.index("b")
print("The index value of b is {}".format(ind_val))

lstx.insert(1,"x")
print("The list after inserting is {}".format(lstx))
lstx.insert(4,"y")
print("The list after inserting y is {}".format(lstx))

# sort, max, min
lstz = [3, 2, 6, 1, 5, 4]
lstz.sort()
print("The list after sorting is {}".format(lstz))

max_val = lstz[-1]
print("the one way of getting maximum value {}".format(max_val))
min_val = lstz[0]
print("the one way of getting minimum value {}".format(min_val))
sec_max_val = lstz[-2]
print("The second highest value is {}".format(sec_max_val))

lstc = [30, 10, 50, 100, 60]
lstc_max = max(lstc)
print("the other way getting maximum value is {}".format(lstc_max))
lstc_min = min(lstc)
print("the other way of getting maximum value is {}".format(lstc_min))

# count
lstm = ["a", "b", "c", "a", "d"]
cnt_a = lstm.count("a")
print("The count of a in lstm is {}".format(cnt_a))
cnt_c = lstm.count("c")
print("the count of c in lstm is {}".format(cnt_c))

