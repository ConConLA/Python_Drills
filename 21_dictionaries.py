# DT-21 DICTIONARIES
# Points: 10
# ----------------------------
# DEFINITION: An key/value store of data 
# 
# 1. Key and value are required, together. 
# 2. Begin and end with curly brackets {}
# 3. Keys are unique.
# 
# Read: https://realpython.com/python-dicts/
# =============================

# A dictionary is a key/value store. 
# Dictionary keys are unique -- they cannot be duplicated. 
foods_list = []


# This is a dictionary. Each entry has a key and value. 
food_emoji = {
    'orange': '🍊',
    'apple': '🍎',
    'lemon': '🍋',
    'watermelon': '🍉',
    'grapes': '🍇',
    'avocado': '🥑',
    'kiwi': '🥝',
    'carrot': '🥕',
    'corn': '🌽'
}

# Access the values by using their keys. Keys must be valid or you'll get a KeyError
print(food_emoji['orange'])
print(food_emoji['corn'])
# food_emoji['salad']  <---------- KeyError: it doesn't exist!


# METHOD: dict.get(key_name)
# Another way to retrieve values is this method:
print(food_emoji.get('lemon'))
print(food_emoji.get('salad'))  # <---------- NO ERROR! It will return None. 


# TASK 1: INTRO
# Create a new dictionary named contact. 


# Add the following key/value pairs: first_name, last_name, address
# Set their values to your name and address


# Add a new property: age whose value is your age. 


# Change the value of address to 2323 Broadway


# Add a new property, city whose value is Oakland


# Add anew property state whose value is California. 


# Print the keys of the dictionary. 


# Print the values of the dictionary. 


# TASK 2: FOOD DICTIONARIES
# Create a new dictionary for the foods below with the following properties:
# name, is_sweet, emoji
# Set their values accordingly. Use the food emoji dictionary.


# Create a new dictionary named apple with the same properties. 
# Add it to the food list.

# Create a new dictionary named lemon with the same properties. 
# Add it to the food list.


# Create a new dictionary named watermelon with the same properties. 
# Add it to the food list.


# Create a new dictionary named grapes with the same properties.
# Add it to the food list.


# Create a new dictionary named corn with the same properties.
# Add each fruit to the food list. 


# Create a new dictionary named avocado with the same properties.
# Add each fruit to the food list. 


# Create a new dictionary named carrot with the same properties.
# Add each fruit to the food list. 


# Print the name and emoji for each food that is sweet.


# Print the emoji for each food that is red. 


# Print the emoji for each food that contains the letter 'o'


# Print all the properties of each food in a nicely formatted row 
# EX.: 🥬 Lettuce Green 

