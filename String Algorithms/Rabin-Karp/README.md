# Rabin-Karp
Rabin-Karp is a pattern matching algorithm introduced in 1987 by Richard M. Karp and Michael O. Rabin. It has a signaficantly low complexity compared to the naive approach.
The idea is to calculate and assign a signature to the pattern and do the same for the elements in a rolling window that iterates over the text. This signature is a *hash value* created by a *hash function*. Then, if the values of the signatures are equal, there is a possible match. Therefore, the algorithm will run a character by character comparison to make sure if there's a match. However, if the signatures don't match, there's definately no match and the window will shift one step to the right.
This is a great approach to solving similar problems with one draw-back. Considering the situation where all the signatures are equal to the pattern's signature. In this situation we're simply doing a character by character comparison which costs **O(nm)**. Consider the following example:
<p align = center>pattern = "bra"</p>
<p align = center>text = "abracadabra"</p>

```
|b|r|a|
|a|b|r|a|c|a|d|a|b|r|a|
```
## Hash
As mentioned before, the algorithm creates and assigns a hash value to each sequence (the pattern and the sequence in the rolling window). This will make the comparisons easier, since comparing integers is much more efficient than comparing strings. 
A hash is considered as a numerical fingerprint of the data created by a hash funcion. Although, there is a range of different forms of hash functions for various purposes, Rabin-Karp uses a poly nomial rolling hash  because it is easier to update.
<p align = center>H($x_0$, ..., $x_{m-1}$) = ($x_0$ * $128^{m-1}$ + $x_1$ * $128^{m-2}$ + ... + $x_{m-2}$ * 128 + $x_{m-1}$) **mod** P</p>
This formula treats the string as a number in base 128. Every character here such as $x_0$ is replaced with its ASCII equivalent. 

### what is **ASCII**?
ASCII is an encoding method. Computers must store everything in numbers. For example each letter must be represented by a number. Encodings defines rules for such matters.
```
'A' --> 65
'B' --> 66
'a' --> 97
```
ASCII is one of the oldest character encodings for English letters, digits, punctuations, control characters using numbers in range of 0 to 127. Total of 128 numbers.
Now you might think this is not enough for all languages in the world. You're right. There are other encodings such as *Unicode* that assigns a unique number to nearly every human language.
```ord(character)``` function takes a character and returns its unicode point, ```chr(number)``` does the opposite.
### what is the p in the formula?
It represents a large prime number. The idea is to use it as modulus to keep the hash value small, because as you can see with only a multiplication the value might explode. Prime numbers tend to work better and prevent collisons--when there are two different strings with equal hash value.
## ROlling Hash
Instead of calculating the value of the hash from scratch everytime, the algorithm simply updates the value. Since there are equal number of operations everytime, the complexity is in constant time O(1) making much efficient.
<p align = center>$H_{new}$ = ($H_{old}$ - $x_0$ * $128^{m-1}$)* 128 + $x_3$ </p>

### Visual example
```
pattern = "bra"
text = "abracadabra"

first window = "abr"
a = 97
b = 98
r = 114
and the pattern = [98, 114, 97]

We will ignore the mod for simplicity in the example

h("bra") = 98 * 128^2 + 114 * 128 + 97
h("bra") = 1620321
h("abr") = 97 * 128^2 + 98*128 + 114
h("abr") = 1601906
comparison: Not equal

Slide the window:
m = 3
outgoing character: x_0
incoming character: x_3
h_new = (16011906 - 97 * 128^2) * 128 + 97 = 1620321
Comparison: Equal
Now character by character comparison.
```
## Complexity
Complexity of this code is O(m +n) just like KMP. However as mentioned before in the worst case senario in which every window has the same hash as the pattern, the complexity rises to O(mn). Simply because it is operating character by character comparisons.
## Refrences
<p>[1] Richard M. Karp; Michael O. Rabin; Efficient randomized pattern-matching algorithms.</p>
<p>[2] Christoph Dürr and Jill-Jênn Vie. Competitive Programming in Python: 128 Algorithms to Develop Your Coding Skills.</p>
