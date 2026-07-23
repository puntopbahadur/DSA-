#1. What is time complexity?
#The Rate of increase in time taken by an algorithm with respect to the input size.

#-----------------------------------------------
#TC -> Big -Oh Notation - > O(3N)
# N -> No of input

# i = 1, i<6, i+=1
for i in range(1, 6):
    print("Abhishek")

#5 X 3 = 15
#N X 3 = 3N

#1. Always calculate TC in terms of worst case
#2. Avoid the constant values
#3. Avoid lower Bound

#1. Always calculate TC in terms of worst case
#=======================================================

#age = ?
age = int(input("Enter your age"))
if age >= 80:
    print("Super Senior")
elif age >= 60 and age < 80:
    print("Senior")
elif (age >= 24 and age <60):
    print("Working")
elif(age >=60 and age <24):
    print("Teen age")
else:
    print("Baby")                


# If the age is 90, it will be only a 2 Operation - Best Case
# If the age is 10, it will be a 5 Operations = Worst Case
# Average case = 2 + 5/2

#==========================================================
#Example 2: Linear Search
arr = [10, 20, 30, 40, 50]

target = 50

for num in arr:
    if num == target:
        print("Found")
        break


# Best Case

# Target = 10
# 10 == 10 ✔
# Only 1 comparison
# Time Complexity: O(1)    
#===================================================
# Worst Case

# Target = 50

# 10 == 50
# 20 == 50
# 30 == 50
# 40 == 50
# 50 == 50 ✔

# 5 comparisons

# Time Complexity: O(n)

# Target Not Found
# 10
# 20
# 30
# 40
# 50

# Checks every element.

# Worst Case = O(n)

#=================================================
# Example 3: Finding Maximum
arr = [5, 9, 3, 8, 2]

maximum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num

# Regardless of the values:

# 5 elements → 5 iterations
# 100 elements → 100 iterations
# 1 million elements → 1 million iterations

# Best Case = Worst Case = O(n)


#===========================================
#Avoid Constant values
# When analyzing time complexity, you ignore constant values and lower-order terms because they do not significantly affect the algorithm's growth as the input size (n) becomes very large.

# For example:

# Actual Operations	       Time Complexity
# 5	                        O(1)
# 100	                    O(1)
# n + 5	                    O(n)
# 2n + 10	                O(n)
# 3n² + 5n + 20	            O(n²)
# n² + n	                O(n²)
# n³ + 100n² + 500	        O(n³)

#====================================================================================
# Rule 1: Ignore Constants
# for i in range(n):      # n operations
#     print(i)

# for j in range(n):      # n operations
#     print(j)

# Total operations:

# n + n = 2n

# Ignore the constant 2:

# O(2n) = O(n)

#=========================================================
# Rule 2: Ignore Lower-Order Terms
# for i in range(n):          # n
#     print(i)

# for i in range(n):
#     for j in range(n):      # n²
#         print(i, j)

# Total operations:

# n² + n

# The n² term grows much faster than n, so we ignore the lower-order term:

# O(n² + n) = O(n²)

#================================================
# Interview Tip

# When simplifying time complexity:

# Remove constants (e.g., 5, 10, 2).
# Remove constant multipliers (e.g., 2n → n, 100n² → n²).
# Keep only the fastest-growing term.

# For example:

# 3n² + 7n + 15
# ↓
# Ignore 7n and 15
# ↓
# Ignore coefficient 3
# ↓
# O(n²)

#=========================================
#Different types of time complexity?
#1. Big - Oh(O) - Worst-case time complexity - Upper Bound
#2. Big Theta (Θ) - Average  Tight Bound 
#3. Big Omega (Ω) - Best-case time complexity - Lower Bound

#Note - Big Theta (Θ) 
#When the best case and worst case grow at the 
# same rate (often described as the average/expected growth
#  in introductory courses, but technically it is a tight bound, not simply average case)

#============================================================================

#Example 

# for i in range(1, n+1):
#     for j in range(1, n+1):

# i       j
# 1       1, 2, 3, 4....N - N   
# 2       1, 2, 3, 4....N - N    
# 3       1, 2, 3, 4....N - N  
# .
# .
# .
# N       1, 2, 3, 4....N - N  

# N + N + N..
# NXN
# O(N2)

#===================================================
#2. Example
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i,j)

# Step 1: Outer Loop

# The outer loop runs from 1 to n.

# Number of iterations = n

# Step 2: Inner Loop

# The inner loop depends on i.

# When i = 1, it runs 1 time.
# When i = 2, it runs 2 times.
# When i = 3, it runs 3 times.
# ...
# When i = n, it runs n times.
# So the total number of iterations is:
# 1 + 2 + 3 + ... + n
# This is the sum of the first n natural numbers.

#======================================================================
# What is Space Complexity?
# Big -Oh Notation
# Space Complexity is the amount of memory (RAM) an algorithm uses as the input size (n) increases.

# It includes:
# 1. Input space (memory needed to store the input) – often not counted when analyzing the algorithm.
# 2. Auxiliary space (extra memory used by the algorithm) – this is what interviewers usually care about.

# Interview Definition
# Space Complexity is the amount of extra memory an algorithm requires to execute with respect to the input size (n).

x = 5
y = 10
z = 7
total = x + y + z
print(total)

# x, y z = Input Space - The space used to store input
# total = Auxiliary space - The extra space used to solve the problem