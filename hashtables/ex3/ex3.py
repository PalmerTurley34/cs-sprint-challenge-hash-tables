def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dicts = []
    result = []
    for array in arrays:
        dicts.append({array[i]:i for i in range(len(array))})

    # find the intersection of the first two dicts
    for key, value in dicts[0].items():
        if key in dicts[1]:
            result.append(key)

    # cross reference that result with the rest of the dicts, removing items when needed
    for dictionary in dicts[2:]:
        for num in result:
            if num not in dictionary:
                result.remove(num)


    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
