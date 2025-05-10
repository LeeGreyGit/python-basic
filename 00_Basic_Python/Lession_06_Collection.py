# Lession 6 : Collection
# Tuple, Array/List, Dictionary

# Use Tuple : Can't add or remove data in list
size = (100, 80)
height = size[0]
width = size[1]

print(size)
print(height)
print(width)

# size = (100, 80, 150)
new_size = size + (150,) # Add long is 150
print(new_size)

# del new_size : delete value new_size

print(len(new_size)) # lenght new_size
print(max(new_size)) # max value in new_size
print(min(new_size)) # min value in new_size


# Use Array/List : use array the same list
damage = [3, 5, 9, 10, 20] # value type in list able multiple
first_damage = damage[0]
damage[0] = 5 # first_damage is not change
print(damage)
print(first_damage)

damage.append(30)
damage.append(9)

# Dictionary : register data in key and value
start_point = {'P1': 50, 'P2':100, 'P3': 150}
print(start_point.keys())
print(start_point.values())
print(start_point['P1'])







