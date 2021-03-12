def repeatedString(s, n):
    """
    :param s: a string to be repeated an infinite ammount of times
    :param n: the first n characters of the infinite string
    :return: how many times does the char 'a' appears in the first n chars
    """
    a_in_s = 0
    if n <= len(s):
        for i in range(n):
            if s[i]=='a':
                a_in_s += 1
    else:
        for i in s:
            if i == 'a':
                a_in_s += 1
        other_chars = n%len(s)
        a_in_s *= n//len(s)
        for i in s[:other_chars]:
            if i == 'a':
                a_in_s += 1
    return a_in_s
