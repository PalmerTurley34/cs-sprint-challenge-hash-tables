def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create a dict
    weight_index = {weights[i]: i for i in range(length)}
    # search through the weights to see if the requirements are met
    for weight in weights:
        if limit-weight in weight_index:
            i_1 = weight_index[weight]
            i_2 = weight_index[limit-weight]
            # in case of collisions, find the index that was overwritten in the dict
            if i_1 == i_2:
                i_1 = weights.index(weight)
            # return the indecies in the proper order
            if i_1 > i_2:
                return (i_1, i_2)
            else:
                return (i_2, i_1)

    return None
