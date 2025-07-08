# DT-20 LISTS


# Points: 10
# ----------------------------
# DEFINITION: An ordered group of objects. 
# 
# 1. Changeable. 
# 2. Lists are begin and end with square brackets []
# 
# Read: https://realpython.com/python-lists/. THIS LINK DOES NOT WORK
# =============================

colors: list = ['red', 'green', 'blue', 'yellow', 'black', 'gray', 'white', 'orange']
numbers: list[int] = [32, -7, 803, 2, 0, -107, 55, 231, 10042, 8, -42, 629, 20089]

# MULTI-DIMENSIONAL LISTS
# This is a 2-D list. It's a list with 2 lists inside.
fish: list[str] = [
    ['bass', 'catfish', 'trout', 'shad', 'sunfish', 'crappie', 'rainbow trout'],
    ['blackbass', 'rainbow trout', 'mosquito fish', 'gudgeon', 'black bullhead', 'trout', 'carp']
]

# FLATTENING LISTS
# To flatten a multi-dimensional list, take each item from all lists
# within and put them into a single list. 
flat_fish1 = [item for subfish in fish for item in subfish]
print(flat_fish1)
flat_fish2 = []
for item in fish:
    for fish1 in item:
        flat_fish2.append(fish1)
print(flat_fish2)

print (len(fish[0]),len(fish[1]))


# TASK 1
# Sort the colors list in alphabetical order. Print it. 

print(sorted(colors))

# Print each list backwards
print(colors[::-1])
print(numbers[::-1])
print([sub[::-1]for sub in fish[::-1]])
print(flat_fish1[::-1])

# Sort the numbers list from greatest to lowest. Print it. 
numbers.sort(reverse=True)
print(numbers)

# Print every 3rd item from each list
print(colors[::3])
for i in range(0,len(colors),3):
    print(colors[i])
print(numbers[::3])
for i in range(0,len(numbers),3):
    print(numbers[i])
print(flat_fish1[::3])



# Print every 2nd item of each list, starting at the 2nd item. 
print(colors[1::2])
print(flat_fish1[1::2])
print(numbers[1::2])

# Print the last 2 items of each list. 
print(colors[-2:])
for color in colors[-2:]:
    print(color)
for number in numbers[-2:]:
    print(number)
for f in flat_fish1[-2:]:
    print(f)
# Using the numbers list, create a new list containing only negative numbers. 
neg = []

for number in numbers:
    if number <0:
        neg.append(number)
print(neg)


# Using the numbers list, create a new list containing only positive numbers. 
pos = [num for num in numbers if num>0]
print(pos)

# Using the colors list, create a new list containing colors that contain ... 
# - the letter 'a' 
letter_a = []
for c in colors:
    if 'a' in c:
        letter_a.append(c)
print(letter_a)

# - the letter 'l' 
letter_l: list = [c for c in colors if 'l' in c]
print(letter_l)



# - 4 or less characters
lessthan_4: list= [c for c in colors if len(c)> 4]
print(lessthan_4)

# Combine colors and numbers into 1 new list. Print the new list. 
print(colors+numbers)

# TASK 2
# Print the first item in fish in the fish list.
print(fish[0][0])

# Print each fish capitalized.
#my notes
#go through fish list
#get each item in fish list
#capitalize it 
#print it

for item in fish:
    for i in item:
        print(i.capitalize())
    

# Print the names of fish with names longer thant 5 characters.
for item in fish:
    for name in item:
        if len(name) >5:
            print(name)

# Print the names of fish that start with the letter 'c' 
#go through fish variable
#find ones that start with 'c'
#print them out
start_c = [name for name in flat_fish1 if name.startswith('c')]
for name in start_c:
    print(name)



# Create a new fish list that contains fish names found in all the lists in fish_list. 
same_fish: list = []
fish1 = fish[0]
fish2 = fish[1]

for f in fish1:
    if f in fish2:
        same_fish.append(f)
print(same_fish)

# Using the colors list, create and print a new list for each item. 
# The new list should contain each character of the item. 
# EX. ['pink'] -> ['p', 'i', 'n', 'k']

for color in colors:
    letters = []
    color_name = [color]
    for char in color:
        letters.append(char)
    print(color_name,'->',letters)


