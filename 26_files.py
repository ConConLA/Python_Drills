# DT-26 FILES
# Points: 10
# ----------------------------
# DEFINITION: Data structures practice.
# 1. Proper nouns must be capitalized in all final outputs
#
# Reading: https://docs.python.org/3/library/pathlib.html#reading-and-writing-files
#
# *************** You MUST download the required files to practice the drills below. ******************
# Downloads: 
# https://gitlab.com/steam-labs-code/practice-drills/-/blob/main/wordlists/adjectives/colors.txt
# https://gitlab.com/steam-labs-code/practice-drills/-/blob/main/wordlists/adjectives/appearance.txt
# 
# =============================
from pathlib import Path


# Make sure the path to the downloaded text file is correct:
colors_file_path = 'path/to/colors.txt'
adjectives_file_path = 'path/to/appearance.txt'


# REVIEW
# Pathlib can be used to handle all file operations. Those include:
# creating paths, removing paths, reading and writing.

# Create:
p = Path('example.txt')
p.touch()

# Remove:
p.unlink()


# Create a new Path for each file and assign it to a variable.


# Verify that the path exists.
# Then open the file in read mode. Create a new list 'rows' of each line in the file.


# Create and open a new text file 'colors_random.txt'
# Shuffle and write all colors to the new file (NOT in alphabetical order).


# Create and open a new text file 'short_6.txt'
# Write all colors and adjectives that are exactly 6 characters long to the file.


# Delete 'short_6.txt' file.


# Create and open a new text file 'long_ones.txt'
# Write all colors and adjectives that are 8+ characters long to the file.


# Delete 'long_ones.txt' file.


# Create a new text file 'data.csv'
# Write  the string 'color,adjective' as the first line of the file.


# Add each color and a random adjective, separated by a comma to the file.
# EX. orange,happy


# Print the contents of 'data.csv' as a formatted table.


