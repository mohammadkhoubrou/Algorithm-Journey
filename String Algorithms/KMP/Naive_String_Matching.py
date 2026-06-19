'''
Naive pattern search method
'''
def search_pattern(s, t):
    n, m, ci = len(s), len(t), 0 #length of text string, target pattern and an index counter
    while True:
        if ci + m < n: #continues untill the end of the string
            if s[ci: ci+m] == t: #comparing a slice of the string with the pattern
                return ci #returns the first index where matching was True
            else: 
                ci += 1
        else:
            return -1

def search_pattern2(s,t):

    n, m =  len(s), len(t)       
    out = [ci for ci in range(n - m, 0, -1) if s[ci: ci + m] == t]
    if len(out) < 1:
        return -1
    return out #returns all the indexes where matching was True
