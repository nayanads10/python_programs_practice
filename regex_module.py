import re

# Search

txt_a = "Its raining at my place"
x = re.search("raining", txt_a)
if x:
    print("Searched successfully")
else:
    print("No match")

y = re.search("^Its.*place$", txt_a)
if y:
    print("Yes, match is successful")
else:
    print("No, Match found")

# find all
txt_b = "The rain in spain"
a = re.findall("ai", txt_b)
print(a)
b = re.findall("in", txt_b)
print(b)

txt_c = "Its quater 8 in the morning"
z = re.findall("[a-zA-Z]", txt_c)
print(z)
y = re.findall("[0-9]",txt_c)
print(y)
b = re.findall("[1234]", txt_c)
if b:
    print("Pattern matched")
else:
    print("No matches found")

# match
pattern = "^a...3$"
str_b = "abcd3"
res = re.match(pattern, str_b)
if res:
    print("Match successful")
else:
    print("Match unsuccessful")

str_c = "abcdefg3"
res_c = re.match(pattern, str_c)
if res_c:
    print("Match successful")
else:
    print("Match unsuccessful")

str_d = "axyz3"
res_d = re.match(pattern, str_d)
if res_d:
    print("Match successful")
else:
    print("Match unsuccessful")

pattern_a = "^.b...3$"
str_x = "abcdg3"
res_x = re.match(pattern_a, str_x)
if res_x:
    print("Match successful")
else:
    print("Match unsuccessful")

str_x = "John age is 29"
rep = re.sub("\s", "", str_x)
print(rep)

rep_y = re.sub("\d", "a", str_x)
print(rep_y)

rep_z = re.sub("\D","a", str_x)
print(rep_z)


#Assignment
txt_a = "The Floods In Chennai"              #It will take characters b/w a to n
x = re.findall("[a-n]", txt_a)
print(x)
txt_b = "My Number is 123456"                 # Find all digit characters
y = re.findall("\d",txt_b)
print(y)
txt_a = "The Floods In Chennai"              #followed by 3 (any) characters
x = re.findall("Fl...s", txt_a)
print(x)
txt_a = "The Floods In Chennai"               #followed excactly 3 (any) characters
x = re.findall("Fl.{3}s", txt_a)
print(x)
txt_a = "The Floods In Chennai"
x = re.findall("Ch....*i",txt_a)
print(x)
x = re.findall("Ch....+i",txt_a)
print(x)
x = re.findall("Ch....?i",txt_a)
print(x)

x = re.findall("water|flows", txt_a)     #It will wether string contains either or OR
if x:
    print("match successful")
else:
    print("match unsuccessful")
x = re.findall("Floods|Chennai", txt_a)
if x:
    print("match successful")
else:
    print("match unsuccessful")

txt_b = "The rever is flowing"
x = re.findall("\AThe", txt_b)
print(x)
if x:
  print("match successful")
else:
  print("match unsuccessful")

txt = "The rever is flowing"
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")

txt = "The rever is flowing"
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")

txt = "The rever is flowing"
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")

txt = "The rever is flowing"
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")


txt = "The rever is flowing_1 time More"
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")

txt = "The rever is flowing_1 time More"
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")

txt = ("The rever is flowing")
x = re.findall("flowing\Z", txt)
print(x)
if x:
  print("Yes, there is a match")
else:
  print("No match")


txt = "The apple is red in colour"                   # starts with
x = re.findall(r"\bour", txt)
print(x)
if x:
  print("match successful")
else:
  print("match unsuccessful")

txt = "The apple is red in colour"                  #ends with
x = re.findall(r"our\b", txt)
print(x)
if x:
  print("match successful")
else:
  print("match unsuccessful")

x = re.findall(r"\Bour", txt)
print(x)
if x:
  print("match successful")
else:
  print("match unsuccessful")

x = re.findall(r"our\B", txt)
print(x)
if x:
  print("match successful")
else:
  print("match unsuccessful")

