#a = int(input("Enter the value of a: "))
#b = int(input("Enter the value of b: "))

#if a > b:
#  diff = a-b
#  print(diff)
#elif a < b:
#   summation = a+b
#   print(summation)

# another way of writing above code
#if a > b:
#  diff = a-b
#  print(diff)
#else:
#   summation = a+b
#   print(summation)
#
# if condition is only required irrespective of else part
#if a > b:
#   diff = a-b
#   print(diff)
#
#lst_x = [1, 2, 3, 4]
#lst_y = [5, 6, 7, 8]
#len_lst_x = len(lst_x)
#sum_lst_x_y = []
#if len(lst_x)==len(lst_y):
#    for i in range(0, len_lst_x):
#        summation = lst_x[i] + lst_y[i]
#        sum_lst_x_y.append(summation)
#print("the sum of two list are {}".format(sum_lst_x_y))

# using list comprehension
#lst_a = [1, 2, 3, 4]
#lst_b = [5, 6, 7, 8]
#summation = [lst_a[i]+lst_b[i] for i in range(0,len(lst_b)) if len(lst_a)==len(lst_b)]
#print("the sum of two lists using list comprehension is {}".format(summation))

# if lists lengths are not same

#lst_x = [1, 2, 3, 4, 5]
#lst_y = [5, 6, 7, 8]
#len_lst_x = len(lst_x)
#sum_lst_x_y = []
#if len(lst_x)==len(lst_y):
#   for i in range(0, len_lst_x):
#       summation = lst_x[i] + lst_y[i]
#       sum_lst_x_y.append(summation)
#print("the sum of two list are {}".format(sum_lst_x_y))

# check given string is palindrome or not
#str_to_check = input("Enter the value: ")
#str_rev = str_to_check[::-1]
#if str_to_check == str_rev:
#    print("the given string is palindrome")
#elif str_to_check != str_rev:
#    print("The given string is not a palindrome")

#str_a = input("Enter the value: ")
#if str_a == str_a[::-1]:
#    print("The given string is palindrome")
#else:
#    print("The given string is not palindrome")

# check whether the given number is even or odd
#num_to_check = int(input("Enter the value: "))
#if num_to_check % 2 == 0:
#    print("The given number is even")
#else:
#    print("The given number is odd")

#  make a list of even numbers and list of odd numbers from 0 to 20
#even_lst = []
#odd_lst = []
#for i in range(0, 20):
#    if 1 % 2 == 0:
#        even_lst.append(i)
#    else:
#        odd_lst.append(i)
#print("the even numbers from 0 to 20 is {}".format(even_lst))
#print("the odd numbers from 0 to 20 is {}".format(odd_lst))

#even_lst = []
#odd_lst = []
#for i in range(0, 20):
#    if i % 2 == 0:
#        even_lst.append(i)
#    else:
#        odd_lst.append(i)
#print("The even numbers from 0 to 20 is {}".format(even_lst))
#print("The odd numbers from 0 to 20 is {}".format(odd_lst))

# find the largest among a,b,c numbers
#a = int(input("Enter the value of a: "))
#b = int(input("Enter the value of b: "))
#c = int(input("Enter the value of c: "))
#if a > b and a > c:
#    print("a is greater")
#elif b > a and b > c:
#    print("b is greater")
#else:
#    print("c is greater")

#lst_y = [2, 4, 3, 2, 5, 3, 6, 7]
#res_lst = []
#for i in lst_y:
#    if i not in res_lst:
#        res_lst.append(i)
#print("The list after removing duplicates is {}".format(res_lst))

# sort numbers
#lst_c = [23, 78, 12, 10, 56, 90, 50]
#for i in range(0, len(lst_c)-1):
#    for j in range(i+1, len(lst_c)):
#        if lst_c[i] > lst_c[j]:
#            lst_c[i], lst_c[j] = lst_c[j], lst_c[i]
#             temp = lst_c[i]
#             lst_c[i] = lst_c[j]
#             lst_c[j] = temp
#print("The list after sorting is {}".format(lst_c))
#print("the maximum value is {}".format(lst_c[-1]))
#print("The minimum value is {}".format(lst_c[0]))


# factorial
#n= int(input("Enter the value: "))
#factorial = 1
# 0 to 5  n-0*n-1*n-2*n-3*n-4*n-5
#for i in range(n):
#    factorial = factorial*(n-i)
#print("The factorial of {} is {}".format(n, factorial))


# write a program to find multiples of 3 from range 100 to 1000
#multiples_of_3 = []
#for i in range(100, 1001):
#    if i % 3 == 0:
#        multiples_of_3.append(i)
#print("multiples of 3 between 100 to 1000:",multiples_of_3)

#Remove duplicates from the string
#str_a = "happynewyear"
#str_b = str(set(str_a))
#print("the values after removing duplicates is {}".format(str_b))

#write program to list all positive and negative numbers
#numbers = [1, 4, -1, 6, -3, 8, 10, -9, 20, -40, 21, 45, -23, -12, 45, 23, -34, -56, 12]
#positive_numbers = []
#negative_numbers = []
#for num in numbers:
#    if num > 0:
#        positive_numbers.append(num)
#    else:
#        negative_numbers.append(num)
#print("positive numbers:", positive_numbers)
#print("negative numbers:", negative_numbers)






