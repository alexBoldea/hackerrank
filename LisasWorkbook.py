def workbook(n, k, arr):
    """n is the number of chapters
    k is the number of problems per page
    arr is the list of the number of problems in each chapter

    n = 5 (also length of arr)
    k = 3
    arr = [4, 2, 6, 1, 10]

    if a problem number in a chapter is the same as a page number -> add 1"""

    pages_in_chapter = {}
    for i in range(1, n+1):
        pages_in_chapter[i] = arr[i-1]//k + 1 if arr[i-1]%k else arr[i-1]//k # {1: 2, 2: 1, 3: 2, 4: 1, 5: 4}
    page_numbers = {}
    current_page = 1
    for i in range(1, n+1):
        page_numbers[i] = []
        for j in range(pages_in_chapter[i]):
            page_numbers[i].append(current_page)
            current_page += 1
    # page_numbers = {1: [1, 2], 2: [3], 3: [4, 5], 4: [6], 5: [7, 8, 9, 10]}
    magic = 0
    for i in arr:
        for j in range(1, i+1):
            countdown = k
            while k:
                if j in page_numbers[i]:
                    magic += 1
                k -= 1


workbook(5, 3, [4, 2, 6, 1, 10])
