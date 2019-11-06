def equalsWhenOneCharRemoved(x, y):
    s1 = None
    s2 = None
    #if diff isn't 1, False by default
    if len(x) is len(y) + 1:
        s1 = x
        s2 = y
    elif len(y) is len(x) + 1:
        s1 = y
        s2 = x
    else:
        return False
 
    a, b = 0, 0
    diff = False
    while a < len(s1) and b < len(s2):
        if s1[a] != s2[b] and not diff:
            diff = True
            a += 1
        elif s1[a] != s2[b]:
            return False
        else:
            a += 1
            b += 1
    return True