
"""
What is string?
  Strings are immutable data type. a string ia a sequence of characters or a sequence of elements,
  which can be a alphabet, alpha numeric or it can be combination of all two
String is enclosed between " or '

Note:string is immutable since it creates memory space only for the elements defined.
"""

empty_string = ""
str_a = "python"
str_n = "1234"
str_an = "python3.9"

len_str = len(str_an)
print("the length of string is {}".format(len_str))

type_str = type(str_an)
print("the type of variable str_an is {}".format(type_str))

# indexing

str_x = "python"
len_str = len(str_x)
print("the length of string is {}".format(len_str))
strx_zeroeth_ind = str_x[0]
print("zeroeth index value of a strx is {}".format(strx_zeroeth_ind))
strx_first_ind = str_x[1]
print("first index value of strx is {}".format(strx_first_ind))
strx_second_ind = str_x[2]
print("second index value of strx is {}".format(strx_second_ind))
strx_third_ind = str_x[3]
print("third index value of strx is {}".format(strx_third_ind))
strx_fourth_ind = str_x[4]
print("fourth index value of strx is {}".format(strx_fourth_ind))
strx_fifth_ind = str_x[5]
print("fifth index value of strx is {}".format(strx_fifth_ind))

str_y = "welcome to class"
len_str = len(str_y)
print("the length of string is {}".format(len_str))
type_str = type(str_y)
print("the type of variable str_y is {}".format(type_str))
stry_zeroeth_ind = str_y[0]
print("zeroeth index value of a stry is {}".format(stry_zeroeth_ind))
stry_first_ind = str_y[1]
print("first index value of a stry is {}".format(stry_first_ind))
stry_second_ind = str_y[2]
print("second index value of a stry is {}".format(stry_second_ind))
stry_third_ind = str_y[3]
print("third index value of a stry is {}".format(stry_third_ind))
stry_fourth_ind = str_y[4]
print("fourth index value of a stry is {}".format(stry_fourth_ind))
stry_fifth_ind = str_y[5]
print("fifth index value of a stry is {}".format(stry_fifth_ind))
stry_sixth_ind = str_y[6]
print("sixth index value of a stry is {}".format(stry_sixth_ind))
stry_seventh_ind = str_y[7]
print("seventh index value of a stry is {}".format(stry_seventh_ind))
stry_eighth_ind = str_y[8]
print("eighth index value of a stry is {}".format(stry_eighth_ind))
stry_ninth_ind = str_y[9]
print("ninth index value of a stry is {}".format(stry_ninth_ind))
stry_tenth_ind = str_y[10]
print("tenth index value of a stry is {}".format(stry_tenth_ind))
stry_eleventh_ind = str_y[11]
print("eleventh index value of a stry is {}".format(stry_eleventh_ind))
stry_twelveth_ind = str_y[12]
print("twelveth index value of a stry is {}".format(stry_twelveth_ind))
stry_thirteenth_ind = str_y[13]
print("thirteenth index value of a stry is {}".format(stry_thirteenth_ind))
stry_fourteenth_ind = str_y[14]
print("fourteenth index value of a stry is {}".format(stry_fourteenth_ind))
stry_fifteenth_ind = str_y[15]
print("fifteenth index value of a stry is {}".format(stry_fifteenth_ind))


# slicing
Str_y = "welcome to class"
ind0_to_ind4 = str_y[0:4]
print("the value of string from zero to fourth index is {}".format(ind0_to_ind4))
ind1_to_ind5 = str_y[1:5]
print("the value of string from one to fifth index is {}".format(ind1_to_ind5))
ind0_to_ind3 = str_y[0:3]
print("the value of string from zero to third index is {}".format(ind0_to_ind3))
ind2_to_ind8 = str_y[2:8]
print("the value of string from second to eight index is {}".format(ind2_to_ind8))
ind0_to_ind15 = str_y[0:15]
print("the value of string from zero to fifteen index is {}".format(ind0_to_ind15))

# slicing with step size
str_z = "welcome"
len_strz = len(str_z)
print(len_strz)
slc_with_step2 = str_z[0:7:2]           # the length of the strz is 7
print("the value of slicing str z with step size 2 is {}".format(slc_with_step2))
slc_with_step3 = str_z[0:7:3]
print("the value of slicing str z with step 3 is {}".format(slc_with_step3))


# slicing all from right to left
ind3_to_all = str_z[3:]
print("value from 3rd index to all is {}".format(ind3_to_all))
ind1_to_all = str_z[1:]
print("value from 1st index to all is {}".format(ind1_to_all))
till_ind5 = str_z[:5]
print("value till 5th index is {}".format(till_ind5))
till_ind3 = str_z[:3]
print("value till 3rd index is {}".format(till_ind3))

# reverse indexing
str_c = "python"
ind1_neg = str_c[-1]
print("value of negative index one is {}".format(ind1_neg))
ind2_neg = str_c[-2]
print("value of negative index two is {}".format(ind2_neg))
ind3_neg = str_c[-3]
print("value of negative index three is {}".format(ind3_neg))
ind4_neg = str_c[-4]
print("value of negative index four is {}".format(ind4_neg))
ind5_neg = str_c[-5]
print("value of negative index five is {}".format(ind5_neg))
ind6_neg = str_c[-6]
print("value of negative index six is {}".format(ind6_neg))



# string concatination
str1 = "welcome"
str2 = "john"
str_res = str1+" "+str2
print("value after concatinating is {}".format(str_res))
str3 = "welcome"
str4 = "to"
str5 = "python"
str6 = "class"
str_res = str3+" "+str4+" "+str5+" "+str6
print("value after concatinating is {}".format(str_res))

# capitalize - it will capitalize first character of string
stra_a = "python"
a = str_a.capitalize()
print("value after capitalizing string is {}".format(a))

# upper case - it converts complete characters in a string into upper case
upp_case = str_a.upper()
print("upper case values are {}".format(upp_case))


# lower case - it converts complete characters in a string into lower case
str_b = "WELCOME"
low_case = str_b.lower()
print("lower case values are {}".format(low_case))
str_c = "HoneY"
low_case = str_c.lower()
print("lower case values are {}".format(low_case))
# upper case
upp_case = str_c.upper()
print("upper case values are {}".format(upp_case))

str_c = "hello"
res = str_c[0:2]+str_c[2:4].upper()+str_c[-1]
print("value after capitalizing only 1 is {}".format(res))
str_d = "sweethome"
res = str_d[0:3]+str_d[3:7].upper()+str_d[-1]
print("value after capitalizing only 1 is {}".format(res))

# to check whether given string is upper
print("the string is upper {}".format(res.isupper()))
str_upp = "HELLO"
print("the string is upper {}".format(str_upp.isupper()))

# to check whether given string is lower
print("the string is lower {}".format(res.islower()))
str_low = "hello"
print("the string is lower {}".format(str_low.islower()))

# title - it will convert into title
str_x = "welcome to python"
tit_str = str_x.title()
print("the value converting it into title is {}".format(tit_str))

# to check whether it is a title or not
print("the string is title {}".format(str_x.istitle()))
print("the string is title {}".format(tit_str.istitle()))

#count
str_a = "welcome"
print("the count of w in string a is {}".format(str_a.count("w")))
print("the count of e in string a is {}".format(str_a.count("e")))

str_x = "Hell0,welcome to class!"
print("the count of l in str x is {}".format(str_x.count("l")))

#index
print("index value of w in str x is {}".format(str_x.index("w")))
print('index value of l in str x is {}'.format(str_x.index("l")))

# strats with
str_a = "hello"
print("the string is starting with h is {}".format(str_a.startswith("h")))
print("the string is starting with i is {}".format(str_a.startswith("i")))
print("thr string is stating with 0 is {}".format(str_a.startswith("o")))

# ends with
print("the string is ending with o is {}".format(str_a.endswith("o")))
print("the string is ending with h is {}".format(str_a.endswith("h")))
print("the string is ending with i is {}".format(str_a.endswith("l")))

