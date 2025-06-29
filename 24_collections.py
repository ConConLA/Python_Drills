# DT-24 COLLECTIONS
# Points: 10
# ----------------------------
# DEFINITION: Data structures practice.
# 
# =============================

make: tuple[str] = ('Ford', 'Chevrolet', 'Oldsmobile', 'Volkswagen')
models: tuple[tuple] = (
    ('Mustang', 'Bronco', 'Corsair', 'Pinto'),
    ('Corvette', 'Impala', 'Chevelle', 'Camaro'),
    ('Cutlass', 'Starfire', 'Aurora', 'Alero'),
    ('Beetle', 'Golf', 'Jetta', 'Transporter')
)
years: list[int] = []
colors: list[str] = ['🔴', '🔵', '🟡', '🟢', '⚫','🟤', '⚪', '🟣', '🟠']

cars: list[dict] = [{'make': 'BMW', 'model': 'S1'}]

# Add all years betwen 1945 and 1980 to the years list.


# Each car has a make and model. Add each car created below to the cars list.
# EX. {'make': 'Toyota', 'model': 'Corolla'}


# Create a dictionary for each model of Ford. 


# Create a dictionary for each model of Chevy.


# Create a dictionary for each model of Oldsmobile.


# Create a dictionary for each model of Volkswagen.


# Each Ford should have a list of random years between 1962-1969. 


# Each Oldsmobile should have a list of random years between 1950-1957. 


# Each Chevy should have a list of random years between 1958-1961. 


# Each Volkswagen should have a list of random years between 1970-1975. 
 

# Remove each year from the years list thats been assigned to any car.


# Add a list of 2 random colors to each car.


# Print a formatted list for each make, followed by each model, year and color.
# EX.
# Toyota:
#   * Corolla   2001, Red
#   * Prius     2012, Black



# =========================== DO NOT EDIT BELOW THIS LINE =============================
for car in cars: print(car)

print(f'Total cars: {len(cars)}')
print(f'Total starting years: 35')
print(f'Remaining years: {len(years)}')
found = set()
for car in cars:
    for color in colors:
        if car.get('colors'):
            if color in car.get('colors'):
                found.add(color)
print(f'Colors not used: {found.difference(colors) if found else "tbd"}')


