def jacobhstal(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2*jacobhstal(n-1)-jacobhstal(n-2)
