def enumerate(n, lst):
	if n==0:
		return x

def p(n,k):
    lst = []
    if n < k:
        return lst
    elif k == 1:
        return lst
    elif k == n:
        return lst
    else:
        p(n-1, k-1) 
        p(n-k, k)
    return lst