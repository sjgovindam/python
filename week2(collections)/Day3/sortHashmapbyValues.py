my_map = {
    "Apple": 50,
    "Banana": 20,
    "Orange": 40,
    "Mango": 10
}

# Ascending
sorted_map = dict(sorted(my_map.items(), key=lambda x: x[1]))

print(sorted_map)

# Descending
sorted_map = dict(sorted(
    my_map.items(),
    key=lambda x: x[1],
    reverse=True
))

print(sorted_map)