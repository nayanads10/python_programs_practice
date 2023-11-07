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