'''
@author:
Date:

'''

###########################################################################
#----------------------GETTING INPUT START--------------------------------#
###########################################################################

# get number of positions from user
print("Enter number of positions: ")
positions = input()

# array to store mass at each position
mass = [int(positions)]


# get mass for each position from user
for i in range(int(positions)):
    print("Enter mass for ", i+1, "position: ")
    # inserting mass in the array
    mass.append(int(input()))

# get assumed frequency from user
print("Enter assumed frequency: ")
assumed_frequency = input()

###########################################################################
#----------------------GETTING INPUT END----------------------------------#
###########################################################################

###########################################################################
#----------------------ALGORITHM IMPLEMENTATION START---------------------#
###########################################################################



###########################################################################
#----------------------ALGORITHM IMPLEMENTATION START---------------------#
###########################################################################