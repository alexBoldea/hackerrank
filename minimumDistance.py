def minimumDistances(a):
    """
    :param a: list of integers

    :return: smallest distance between 2 equal integers // a[i] == a[j] return abs(j-i)
    """
    distance = len(a)
    for i in range(len(a)):
        try:
            if distance > abs(i - (a[i+1:].index(a[i])+i+1)):
                distance = abs(i - (a[i+1:].index(a[i])+i+1))
        except:
            pass

    return distance if distance < len(a) else -1


print(minimumDistances([7,1,3,4,1,7]))
