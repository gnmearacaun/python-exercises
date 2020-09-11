# The number of students in each of the three groups is known.
# Output the smallest number of desks to be purchased.
# Each group will sit in its own classroom.
# The program receives the input of three non-negative integers:
# the number of students in each of the three classes
# (the numbers do not exceed 1000).
# Sample Input 1: 20 21 22
# Sample Output 1: 32
# Sample Input 2: 16 18 20
# Sample Output 2: 27
import math
m_group1 = abs(int(input()))
m_group2 = abs(int(input()))
m_group3 = abs(int(input()))

if m_group1 % 2 == 0:
    desks1 = m_group1 // 2
elif m_group1 % 2 == 1:
    desks1 = math.ceil(m_group1 / 2)

if m_group2 % 2 == 0:
    desks2 = m_group2 // 2
elif m_group2 % 2 == 1:
    desks2 = math.ceil(m_group2 / 2)

if m_group3 % 2 == 0:
    desks3 = m_group3 // 2
elif m_group3 % 2 == 1:
    desks3 = math.ceil(m_group3 / 2)

desks = desks1 + desks2 + desks3
print(desks)
