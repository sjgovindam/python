map1 = {"Apple": 10, "Banana": 20}
map2 = {"Apple": 30, "Orange": 40}

# Merge (map2 overwrites duplicate keys)
result = {**map1, **map2}

print(result)