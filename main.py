# Lab 2: Class Costs
# Author: James Bruestle

# 1. Initialize variables for the:
#    Elms tuition (see https://www.elms.edu/financial-aid/undergraduate/),
#    2 semesters per year, 
#    5 classes per semester, 
#    15 weeks per semester, 
#    and 75 minutes per class.

semPerYear = 2
classPerSemester = 5
weekPerSemester = 15
minPerClass = 75
tuition = 38735

# 2. Cost per course: Using your variables above, calculate and print the cost per course (for example for CIT 2103). 
# Use the tuition for the year, the number of semesters per year, and the number of classes per semester.
costPerCourse = tuition / semPerYear / classPerSemester
print("Cost per course: " + str(costPerCourse))

# 3. Skipped Class: Calculate the cost of a (skipped) class session by using the cost per course you calculated in step 2 and the number of weeks per semester assuming the class meets twice a week.
skipClass = costPerCourse / weekPerSemester
print("Cost per class: " + str(skipClass))

# 4. Cost per minute: Calculate the cost per minute for a class using the cost of a class session that you calculated in step 3 and the number of minutes per class.
costPerMinute = skipClass / minPerClass
print("Cost per minute: " + str(costPerMinute))

# 5. Extra credit: Take your financial aid scholarships (not loans) into account to calculate the costs above with and without financial aid.