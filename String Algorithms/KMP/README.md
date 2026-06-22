# KPM
The Knuth-Morris-Pratt (KMP) algorithm was introduced in 1977 by Donald E. Knuth, James H. Morris, Jr., and Vaughan R. Pratt 
as an solution for string matching problems and successfully achieved a linear-time by avoiding unnecessary comparisons.
Before we begin analyzing the algorithm, let's take a look at the naive approach.
## Naive algorithm
```
def search_pattern2(s,t):

    n, m =  len(s), len(t)       
    out = [ci for ci in range(n - m, 0, -1) if s[ci: ci + m] == t]
    if len(out) < 1:
        return -1
    return out
```
### Time and Space Complexity
In this method we have to go through the whole text and make a comparison for each character in the text. Therefore, the complexity 
of this algorithm is ```O(nm)```. Why? Let's see:

The loop ```for ci in range(n - m, 0, -)``` runs n - m times, so less than n. Therefore the complexity of this part is O(n).
The comparison ```s[ci: ci + m] == t``` costs O(m) where m is the length of each pattern. Simply because it has to compare them character by character.
Best case senario is that the target and the slice don't match right away and the worst case is that the comparison continues untill 
the last character of the slice which is m comparisons.

In each iteration there's a temporary slice with the length m so in each iteration the space complexity is O(m). If there are more 
than one matches (let's say k matches) we will need k spaces to assign to 'out' to store the indexes. 

| Space Time  | Complexity  |
| ---------   | ----------  |
| ***Time***  | **O(nm)**   |
|***Space***  | **O(m + k)**|

## Longest Prefix and Suffix (LSP) border
border is a stric substring or word from the pattern p which at the same time is strict suffix and stric prefix. What is stric? It means that the length of the border must be less than the length of p. A *LSP* is the longest border of a pattern which is indicated with **β(p)**.
```
|a|b|a|a|b|a|b|a|a|
          |a|b|a|a|b|a|b|a|a|
```
*abaa* is the LSP of the sequence *abaababaa*.
Imagine we can set a check point in the pattern matching process for the *last longest border*.
Why is this important? 
Because we will treat the pattern we are looking for in the text, as a border of a portion text.
So we'll have to calculate all the borders of our given text.
```
pattern = abcab
borders: ab
β(ab) = ε --> as we discussed length of a border must be less that the pattern itself and a border is equal suffix and prefix which we don't have here.
-------------------------------------------------------------------------------------------------------------------------------
pattern = abababab
borders: ab, abab, ababab
β(p) = ababab
β(ababab) = abab
β(abab) = ab
β(ab) = ε
```
Then we will store the longest prefix and suffix which we introduced as border in an array (f). How do we do that?
For that we'll iterate over the text with two pointer one of which goes over each element of the text in order(j) and the other incrementally counts the matching sequences up untill that point(k).
Now three cases might emerge. Consider the following pattern:
                                            **abababcabac**
The j pointer is set to index 1. Because when both of them are at 0, they match but the length of pattern is equal to the border we have chosen, so it's not really a border.
1. The two characters of the pattern don't match and k is pointing at the first character, thus k = 0. In this case the $f_i$ is *zero*. There's no prefix that is equal to the suffix.
```
|a|b|a|b|a|b|c|a|b|a|c|
 ^ ^
 k j
```
2. The two characters are equal. Then we increment k and add it to the array. This shows that up until now we have found one border which longest border of this substring. So we know that now k = 1 pointing at b and j = 3 pointing at b. This will go untill we hit a mismatch which is the last case we will discuss.
```
|a|b|a|b|a|b|c|a|b|a|c|
 ^   ^
 k   j
```
3. The two characters are not equal and we have encountered a mismatch. Also the important point is that k is not zero. k has kept the track of the last longest border until now, so we know that there might be a *Fall Back*. If there is, k will look for a border that ends with the character that j is pointing at. If not found, it will continue the fall back until the begining of the array where k = 0 and case 1 is True.
```
|a|b|a|b|a|b|c|a|b|a|c|
         ^   ^
        k=4 j=6

|a|b|a|b|a|b|c|a|b|a|c|
     ^       ^
    k=2     j=6

|a|b|a|b|a|b|c|a|b|a|c|
 ^           ^
k=0         j=6
```
|   $f_i$   |     k      |  Border  |
| --------- | ---------- |----------|
|   $f_0$   |     0      |    ε     |
|   $f_1$   |     0      |    ε     |
|   $f_2$   |     1      |    a     |
|   $f_3$   |     2      |   ab     |
|   $f_4$   |     3      |   aba    |
|   $f_5$   |     4      |   abab   |
|   $f_6$   |     0      |    ε     |
|   $f_7$   |     1      |    a     |
|   $f_8$   |     2      |   ab     |
|   $f_9$   |     3      |   aba    |
|   $f_10$  |     0      |    ε     |

##KMP pattern matching
We'll use a null character to join the pattern and text together. As you can expect, the iteration and counting the longest border continues untill it hits a anomaly and reset the counting. Just like the 'c' character above.
Then we'll look for the border in array that has the same length as the pattern we're looking for.
Once we have found it we will subtract the length of the pattern from the border and add one to it(because of the null character) to get the pattern begining index in the mixed string. Now we must subtract the pattern in the begining plus the null character from it to get the index in the original text string.
### Complexity
Complexity of this algorithm is better that the naive aproach. The complexity is ```O(m + n)``` with m being the length of the pattern and n length of the text. 
Even though there's a nested loop, the complexity is no quadratic (n^2). In the second while loop, k = f[k - 1] cannot happen so many times, since k aquires strictly smaller values every time. The k += 1 part is executed less than n times. So O(n). it is linear.
For KMP function, the toatal length of input is n + 1 + m where n is the length of the pattern and n is the length of the text. So the total complexity is O(n + m).

## Refrences
[1] D. E. Knuth, J. H. Morris, V. R. Pratt. "Fast Pattern Matching in Strings" SIAM Journal on Computing, 1977.
[2] Christoph Dürr and Jill-Jênn Vie. Competitive Programming in Python: 128 Algorithms to Develop Your Coding Skills.
