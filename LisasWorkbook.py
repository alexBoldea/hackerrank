def workbook(n, k, arr):
    """n is the number of chapters
    k is the number of problems per page
    arr is the list of the number of problems in each chapter
    n = 5 (also length of arr)
    k = 3
    arr = [4, 2, 6, 1, 10]
    if a problem number in a chapter is the same as a page number -> add 1"""
    page_problems = {}
    magic = 0
    pages_counted = 1
    for i in arr:
        countdown_from = i        
        problem_no = 1
        while countdown_from:
            page_problems[pages_counted] = []
            if countdown_from//k > 0:
                for _ in range(k):
                    page_problems[pages_counted].append(problem_no)
                    problem_no += 1
                countdown_from -= k
                pages_counted += 1
            elif countdown_from//k == 0:
                for _ in range(countdown_from%k):
                    page_problems[pages_counted].append(problem_no)
                    problem_no += 1
                pages_counted += 1
                countdown_from = 0
            else:
                break
    for i in page_problems.keys():
        if i in page_problems[i]:
            magic += 1
    return magic
