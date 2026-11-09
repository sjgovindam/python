def main():

    my_map = {}

    my_map[30] = "C"
    my_map[10] = "A"
    my_map[20] = "B"
    my_map[40] = "D"

    sorted_map = dict(sorted(my_map.items()))

    print(sorted_map)

    sorted_map_reverse = dict(sorted(my_map.items(), reverse=True))

    print(sorted_map_reverse)


if __name__ == "__main__":
    main()