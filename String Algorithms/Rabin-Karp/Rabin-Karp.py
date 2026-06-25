def hash(string, base, prime):
    h = 0
    for ch in string:
        h = (h * base + ord(ch)) % prime 
    return h

def hash_rolling(bp, old_hash, base, prime, incoming, outgoing): #bp is the base to the power of m-1. it will
    return ((old_hash - outgoing * bp) * base + incoming) % prime #repeat many times that's why It's precalculated.

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = [] #store the indexes of the matches
    if m == 0: #condition where there's no pattern to search for
        return 0
    if m > n: #condition where there's definitely no match
        return -1
    
    base = 128
    prime = 2 ** 31 -1 # any large prime less than 2^56

    pattern_hash = hash(pattern, base, prime)
    window_hash = hash(text[:m], base, prime)
    base_power = (base ** (m-1)) % prime #bp that was introduce before
    if window_hash == pattern_hash and text[:m] == pattern: return 0
    
    for i in range(1, n - m + 1):
        outgoing = ord(text[i -1])
        incoming = ord(text[i + m - 1])

        window_hash = hash_rolling(base_power, window_hash, base, prime, incoming, outgoing)

        if window_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)
    if len(matches) == 0:
        return -1
    return matches #returns all the indexes where there's a mathch

print(rabin_karp("abracadabra", "bra"))