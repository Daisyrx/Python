# -*- coding: utf-8 -*-
"""
Python HW1 02/08/2020

@author: Runxin Yu
"""
# 1.(a)
list1 = []
for i in range(1,21):
    list1.append(i)
print(list1)

# 1.(b)
list2 = []
for k in range(20,0,-1):
    list2.append(k)
print(list2)

# 1.(c)
list3 = list1.copy()
for j in range(19,0,-1):
    list3.append(j)
print(list3)

# 1.(d)
list3 = 10*[4,6,3]
print(list3)

# 1.(e)
list4 = 11*[4,6,3]
del list4[-1]
del list4[-1]
print(list4)

# 2.
list5 = []
import numpy
import math
for x in numpy.arange(3,6,0.1):
    list5.append(round(math.exp(x)*math.cos(x),2))
print(list5) 

# 3.
list6 = []
for y in range(1,26):
    list6.append(round(pow(2,y)/y,2))
print(list6)

# 4.(a)
a = list1.copy()
a_new = [ a[x]- a[-1-x] for x in range(len(a)) ]
print(a_new)


# 4.(b)
a_boolean = [a[x] % 2 == 0 for x in range(len(a))]
print(a_boolean)

# 5.
with open('lorem.txt','r') as f:
    all_lines = f.readlines()
    f.close()

import re
text = ''.join(all_lines)
pat = re.compile('([A-Z][a-z]+)|([a-z]+)')
match = pat.findall(text)
# (a)
word = []
for l in all_lines:
    word.extend(re.split(r'[;,\s,.,:]\s*', l))

word4 =[]
word7 =[]
word8 =[]
for p in word:
    if len(p)>=1 and len(p)<=4:
        word4.append(p)
    elif len(p)>4 and len(p)<=7:
        word7.append(p)
    elif len(p)>=8:
        word8.append(p)
print("The number of strings whose lengths are between 1 and 4 is: %s" % (len(word4)))
print("The number of strings whose lengths are between 4 and 7 is: %s" % (len(word7)))
print("The number of strings whose lengths are 8 or greater is: %s" % (len(word8)))     

# (b)
cap =[]
low = []
for m in match:
    if len(m[0]) > 0:
        cap.append(m[0])
    else:
        low.append(m[1])
print('The number of capitalized characters in the file is: %s\n' % (len(cap)))








    
    
    




















