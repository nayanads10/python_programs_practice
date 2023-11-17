"""
what is tuple?
tuple is immutable, tuples are used to store multiple items or elements or a data in a single variable
it can be a combination of alphabet, numeric or alpha numeric or combination of all 3
tuples are enclosed between ()

Note: tuple is immutable since it creates memory space only for the defined elements, hence we cannot add or
change elements
"""

tpl_emp1 = ()             # one way of defining  empty tuple
tpl_emp = tuple()         # another way of defining empty tuple

tpl_a = ("a","b",1,"python")
print("the items of tuple is {}".format(tpl_a))

# length of tuple
len_tpl_a = len(tpl_a)
print("the length of tuple a is {}".format(len_tpl_a))

# type of tuple
typ_tpl_a = type(tpl_a)
print("the type of tuple a is {}".format(typ_tpl_a))

# difference between list and tuple
"""
list:    * list is mutable
         * list creates extra heap space memory once it is defined
         * list slow
         * time complexity is more
         * once defined elements can be changed 
         * list can be appended and extended
         * list is enclosed between []
         
tuple:   * tuple is immutable
         * tuple creates heap space memory only for the defined elements
         * tuple is faster
         * time complexity is less
         * once defined elements cannot be changed 
         * tuple cannot be extended or appended
         * tuple is enclosed between ()      
"""
# indexing
ind_tpl_a = tpl_a[0]
print("zeroeth element of tuple a is {}".format(ind_tpl_a))
ind_tpl_a = tpl_a[1]
print("first element of tuple a is {}".format(ind_tpl_a))
ind_tpl_a = tpl_a[2]
print("second element of tuple a is {}".format(ind_tpl_a))
ind_tpl_a = tpl_a[3]
print("third element of tuple a is {}".format(ind_tpl_a))

# indexing
tpl_z = (1,2,"home","c","d")
ind_tpl_z = tpl_z[0]
print("zeroeth element of tuple z is {}".format(ind_tpl_z))
ind_tpl_z = tpl_z[1]
print("first element of tuple z is {}".format(ind_tpl_z))
ind_tpl_z = tpl_z[2]
print("second element of tuple z is {}".format(ind_tpl_z))
ind_tpl_z = tpl_z[3]
print("third element of tuple z is {}".format(ind_tpl_z))
ind_tpl_z = tpl_z[4]
print("fourth element of tuple z is {}".format(ind_tpl_z))

# slicing
tpl_y = (1,2,"home","c","d","f")
ind0_to_ind4 = tpl_y[0:4]
print("the value of tuple from zero to fourth is {}".format(ind0_to_ind4))
ind1_to_ind6 = tpl_y[1:6]
print("the value of tuple from one to sixth is {}".format(ind1_to_ind6))
ind3_to_ind5 = tpl_y[3:5]
print('the value of tuple from three to five is {}'.format(ind3_to_ind5))

# slicing with step size
len_tply = len(tpl_y)
print(len_tply)
print("the length of tuple y is {}".format(len_tply))
slc_with_stp2 = tpl_y[0:6:2]
print("the value of slicing tpl y with step 2 is {}".format(slc_with_stp2))
slc_with_stp3 = tpl_y[0:6:3]
print("the value of slicing tpl y with step 3 is {}".format(slc_with_stp3))

# index
tpl_b = ("John", "Alex", "Bob", "xyz")
ind_bob = tpl_b.index("Bob")
print("The index value of bob is {}".format(ind_bob))

# count
cnt_john = tpl_b.count("John")
print("The count of John in tuple b is {}".format(cnt_john))


