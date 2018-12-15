'''
@author:
Date:

'''

###########################################################################
#----------------------GETTING INPUT START--------------------------------#
###########################################################################

# get number of positions from user
print("Enter number of positions: ")
positions = int(input())

# array to store mass at each position
mass = [int(positions)]


# get mass for each position from user
for i in range(int(positions)):
    print("Enter mass for ", i+1, "position: ")
    # inserting mass in the array
    mass.append(int(input()))

# get assumed frequency from user
print("Enter assumed frequency: ")
assumed_frequency = float(input())

###########################################################################
#----------------------GETTING INPUT END----------------------------------#
###########################################################################

###########################################################################
#----------------------ALGORITHM IMPLEMENTATION START---------------------#
###########################################################################
defelction = float(1)
columnThird = []
deflection_cal = []
summation = float(0)
stiffness = float(1000)
residual = float(0)

deflection_cal.append(1)

for i in range(1, positions+1):

    val = float(mass[i])*assumed_frequency*assumed_frequency
    val = val * defelction
    columnThird.append(float(val))

    for j in range(i):
        summation = summation + columnThird[j]
    summation = summation/stiffness

    if i == positions:
        residual = summation
    defelction = deflection_cal[i-1] - summation
    deflection_cal.append(defelction)
    summation = 0

###########################################################################
#----------------------ALGORITHM IMPLEMENTATION END---------------------#
###########################################################################


# final output
print(residual)