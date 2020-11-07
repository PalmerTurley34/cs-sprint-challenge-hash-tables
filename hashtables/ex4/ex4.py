def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # dict with key being the positive int and value is the count of neg ints
    result = []
    my_dict = {}
    for num in a:
        if num not in my_dict:
            my_dict[num] = 1
            if num*-1 in my_dict:
                if my_dict[num] == 1 and my_dict[num * -1] == 1:
                    if num > 0:
                        result.append(num)
                    elif num <0:
                        result.append(num * -1)
        else:
            my_dict[num] += 1
    return result

         


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
