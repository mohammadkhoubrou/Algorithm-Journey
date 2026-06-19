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
of this algorithm is O(nm). Why? Let's see:

The loop ```for ci in range(n - m, 0, -)``` runs n - m times, so less than n. Therefore the complexity of this part is O(n).
The comparison ```s[ci: ci + m] == t``` costs O(m) where m is the length of each word. Simply because it has to compare them character by character.
Best case senario is that the target and the slice don't match right away and the worst case is that the comparison continues untill 
the last character of the slice which is m comparisons.

In each iteration there's a temporary slice with the length m so in each iteration the space complexity is O(m). If there are more 
than one matches (let's say k matches) we will need k spaces to assign to 'out' to store the indexes. 

| Space Time  | Complexity  |
| ---------   | ----------  |
| ***Time***  | **O(nm)**   |
|***Space***  | **O(m + k)**|

## Maximal-Boundries
Boundry is a stric substring or word from the word w which at the same time is strict suffix and stric prefix. What is stric? It means that the length of the boundry must be less than the length of w. A *Maximal-Boundry* is the longest boundryof a word which is indicated with **β(w)**.
```
|a|b|a|a|b|a|b|a|a|
          |a|b|a|a|b|a|b|a|a|
```
*abaa* is the maximal-boundry of the word *abaababaa*.
Imagine we can set a check point in the pattern matching process for the *last longest boundry*. The important point is that each boundry has its own boundry, and each of those boundries have their own.
