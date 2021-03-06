def surfaceArea(A):
    """
    A = integer array of arrays
    return = total surface
    """
    
    # surface = 2 * numbers in A (this covers top and bottom surfaces) +
    #           row lateral surfaces = first elem + abs(second - first) + ... + last elem +
    #           column lateral surfaces = first elem + abs(first of second - first of first) + ...
    bottom = 0
    for i in A:
        bottom += len(i)
    bottom *= 2

    rowSurf = 0
    for i in A:
        rowSurf += i[0]
        for j in range(1, len(i)):
            rowSurf += abs(i[j]-i[j-1])
        rowSurf += i[-1]

    colSurf = 0
    colSurf += sum(A[0])
    for i in range(len(A[0])):        
        for j in range(1, len(A)):
            colSurf += abs(A[j][i] - A[j-1][i])
    colSurf += sum(A[-1])
    totalSurf = bottom + rowSurf + colSurf # sum all
    return totalSurf
