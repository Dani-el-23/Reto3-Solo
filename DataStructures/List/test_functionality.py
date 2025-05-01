from DataStructures.List import array_list as al


# 🛠 TESTING THE MERGE SORT FUNCTION 🛠
if __name__ == "__main__":
    # Create a new array_list
    test_list = al.new_list()

    # Add elements to the list
    elements_to_add = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    for elem in elements_to_add:
        al.add_last(test_list, elem)

    print("Before Sorting:", test_list["elements"])

    # Apply merge sort
    sorted_list = al.merge_sort(test_list)

    print("After Sorting:", sorted_list["elements"])
