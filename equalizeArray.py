def equalizeArray(arr):
    """

    :param arr: list of integers
    :return: len(arr) - count of most common element
    """
    arr_dict = {}
    for i in arr:
        if i in arr_dict:
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1
    return len(arr) - max(arr_dict.values())
