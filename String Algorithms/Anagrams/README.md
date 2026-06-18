# Anagrams
Anagram refers to a word that was created by rearranging the letters of another word. 
Here is an illustration of anagrams:
```
cat --> act
stop --> post
heart --> earth
```
## Code Explanation
The idea is to create a signature for each word in the input text. And check the next word in the string for its signature.
If it matches the signature of any other word that we have seen before, then it's a anagram of that word. However, if there's no
similar signature among the previous words, this word doesn't have an anagram yet, so we add it to the dictionary by itself.
And what better signature than the characters of each word itself.
## Complexity
### Time complexity
If we seperately calculate the complexity of each section of the algorithm, we'll see:
``` S.split() ``` has a complexity of O(nk) where n is the number of words and k is the average length of a word. Creating a 
tuple consisting of the processed words, O(n).
```for word in S```, O(n)
```sorted(word)``` has a complexity of O(k log k), repeating that for all words, O(n.k log k).
The dictionary operations are O(1) and across all words, O(n).
```[d[s] for s in d if len(d[s]) > 1]``` doesn't append all the elements, only those with length over 1. Therefore, the number of
iterations is less than n.
In general, the dominant term is ```O(n.k log k)```, so that's our complexity.

### Space complexity
The dictionary stores up to n words. Each word with k characters, ```O(nk)```.
